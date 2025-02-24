"""
This module can be used to run the actions in a way that the actions are pre-loaded
(i.e.: imported) but no actions are actually run until requested by the action-server.

Important: this will run in the target environment and can't really import anything
from the action server.
"""
import argparse
import os
import sys
import traceback

DEFAULT_TIMEOUT = 10
NO_TIMEOUT = None
USE_TIMEOUTS = True


class _DummyStdin(object):
    def __init__(self, original_stdin=sys.stdin, *args, **kwargs):
        try:
            self.encoding = sys.stdin.encoding
        except:
            # Not sure if it's available in all Python versions...
            pass
        self.original_stdin = original_stdin

        try:
            self.errors = (
                sys.stdin.errors
            )  # Who knew? sys streams have an errors attribute!
        except:
            # Not sure if it's available in all Python versions...
            pass

    def readline(self, *args, **kwargs):
        return "\n"

    def read(self, *args, **kwargs):
        return self.readline()

    def write(self, *args, **kwargs):
        pass

    def flush(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass


def binary_stdio():
    """Construct binary stdio streams (not text mode).

    This seems to be different for Window/Unix Python2/3, so going by:
        https://stackoverflow.com/questions/2850893/reading-binary-data-from-stdin
    """
    PY3K = sys.version_info >= (3, 0)

    if PY3K:
        stdin, stdout = sys.stdin.buffer, sys.stdout.buffer
    else:
        # Python 2 on Windows opens sys.stdin in text mode, and
        # binary data that read from it becomes corrupted on \r\n
        if sys.platform == "win32":
            # set sys.stdin to binary mode
            import msvcrt

            msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
            msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
        stdin, stdout = sys.stdin, sys.stdout

    # The original stdin cannot be used and anything written to stdout will
    # be put in the stderr.
    sys.stdin, sys.stdout = (_DummyStdin(), sys.stderr)

    return stdin, stdout


def socket_connect(host, port):
    import socket as socket_module

    s = socket_module.socket(socket_module.AF_INET, socket_module.SOCK_STREAM)

    #  Set TCP keepalive on an open socket.
    #  It activates after 1 second (TCP_KEEPIDLE,) of idleness,
    #  then sends a keepalive ping once every 3 seconds (TCP_KEEPINTVL),
    #  and closes the connection after 5 failed ping (TCP_KEEPCNT), or 15 seconds
    try:
        s.setsockopt(socket_module.SOL_SOCKET, socket_module.SO_KEEPALIVE, 1)
    except (AttributeError, OSError):
        pass  # May not be available everywhere.
    try:
        s.setsockopt(socket_module.IPPROTO_TCP, socket_module.TCP_KEEPIDLE, 1)
    except (AttributeError, OSError):
        pass  # May not be available everywhere.
    try:
        s.setsockopt(socket_module.IPPROTO_TCP, socket_module.TCP_KEEPINTVL, 3)
    except (AttributeError, OSError):
        pass  # May not be available everywhere.
    try:
        s.setsockopt(socket_module.IPPROTO_TCP, socket_module.TCP_KEEPCNT, 5)
    except (AttributeError, OSError):
        pass  # May not be available everywhere.

    try:
        # 10 seconds default timeout
        s.settimeout(DEFAULT_TIMEOUT if USE_TIMEOUTS else NO_TIMEOUT)
        s.connect((host, port))
        s.settimeout(None)  # no timeout after connected
    except:
        raise RuntimeError("Could not connect to %s: %s", host, port)

    rfile = s.makefile("rb")
    wfile = s.makefile("wb")
    return rfile, wfile


def add_arguments(parser):
    parser.description = "Preload action-server actions"

    parser.add_argument(
        "--tcp", action="store_true", help="Use TCP server instead of stdio"
    )
    parser.add_argument("--host", default="127.0.0.1", help="Bind to this address")
    parser.add_argument("--port", default=-1, type=int, help="Bind to this port")


class MessagesHandler:
    def __init__(self, read_stream, write_stream):
        try:
            from preload_actions_streams import (  # type: ignore
                JsonRpcStreamReaderThread,
                JsonRpcStreamWriter,
            )
        except ImportError:
            from .preload_actions_streams import (
                JsonRpcStreamReaderThread,
                JsonRpcStreamWriter,
            )

        from queue import Queue

        self._readqueue = Queue()
        self._jsonrpc_stream_reader = JsonRpcStreamReaderThread(
            read_stream, self._readqueue, self._on_message
        )
        self._jsonrpc_stream_writer = JsonRpcStreamWriter(write_stream)

    def start(self):
        import io
        from contextlib import redirect_stderr, redirect_stdout

        self._jsonrpc_stream_reader.start()

        # Collect actions so that it's ready to go when requested.
        s = io.StringIO()
        try:
            from robocorp.actions import cli

            with redirect_stdout(s), redirect_stderr(s):
                cli.main(["list"], exit=False)
        except BaseException:
            print(s.getvalue())
            traceback.print_exc()

        while True:
            msg = self._readqueue.get()
            self._on_message(msg)

    def _on_message(self, message):
        # Original command line is something as:
        # python = get_python_exe_from_env(env)
        # cmdline: List[str] = [
        #     python,
        #     "-m",
        #     "robocorp.actions",
        #     "run",
        #     "--preload-module",
        #     "preload_actions",
        #     "-a",
        #     action.name,
        # ]
        #
        # cmdline.append(str(action.file))
        # cmdline.append(f"--json-input={input_json}")

        # Some things must be set in the environment for the run:
        #
        # env["ROBOT_ARTIFACTS"] = robot_artifacts
        # env["RC_ACTION_RESULT_LOCATION"] = result_json
        #
        # for key, value in headers.items():
        #     if value:
        #         env[key.upper()] = value
        command = message.get("command")
        if command == "run_action":
            from robocorp.actions import cli

            returncode = 1
            try:
                action_name = message["action_name"]
                action_file = message["action_file"]
                input_json = message["input_json"]
                robot_artifacts = message["robot_artifacts"]
                result_json = message["result_json"]
                headers = message["headers"]

                os.environ["ROBOT_ARTIFACTS"] = robot_artifacts
                os.environ["RC_ACTION_RESULT_LOCATION"] = result_json
                if headers:
                    for key, value in headers.items():
                        if key and value:
                            os.environ[key.upper()] = value

                # The preloaded actions must be always in place.
                sys.modules.pop("preload_actions", None)
                args = [
                    "run",
                    "--preload-module",
                    "preload_actions",
                    "-a",
                    action_name,
                    action_file,
                    f"--json-input={input_json}",
                ]
                returncode = cli.main(args, exit=False)
            except BaseException:
                traceback.print_exc()

            finally:
                self._jsonrpc_stream_writer.write({"returncode": returncode})


def main(args=None):
    original_args = args if args is not None else sys.argv[1:]

    parser = argparse.ArgumentParser()
    add_arguments(parser)

    args = parser.parse_args(args=original_args)

    if args.tcp:
        rfile, wfile = socket_connect(args.host, args.port)
    else:
        rfile, wfile = binary_stdio()

    server = MessagesHandler(rfile, wfile)
    server.start()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Critical error (the logging may not be set up properly).
        traceback.print_exc()
