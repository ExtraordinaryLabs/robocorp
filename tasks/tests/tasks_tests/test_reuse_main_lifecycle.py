import subprocess
import sys
from subprocess import CalledProcessError


def test_reuse_main_lifecycle(datadir, str_regression):
    target = datadir / "main.py"
    try:
        output = subprocess.check_output(
            [sys.executable, str(target)], cwd=str(datadir)
        )
    except CalledProcessError as err:
        print(err.stdout.decode("utf-8"))
        if err.stderr:
            print(err.stderr.decode("utf-8"))
        raise
    print(output.decode("utf-8"))
