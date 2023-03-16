import robocorp_logging
from robocorp_logging._rewrite_config import BaseConfig


class ConfigForTest(BaseConfig):
    def can_rewrite_module_name(self, module_name: str) -> bool:
        return "check" in module_name

    def can_rewrite_module(self, module_name: str, filename: str) -> bool:
        return "check" in module_name


def test_sensitive_data():
    from imp import reload
    from robocorp_logging_tests._resources import check_sensitive_data
    from io import StringIO
    from robocorp_logging import iter_decoded_log_format

    s = StringIO()

    def write(msg):
        s.write(msg)

    with robocorp_logging.setup_auto_logging():
        check_sensitive_data = reload(check_sensitive_data)

        with robocorp_logging.add_in_memory_logging_output(write):
            check_sensitive_data.run()

    assert "my_pass" not in s.getvalue()
    assert "this should not be shown" not in s.getvalue()
    assert "dont_log_this_arg" not in s.getvalue()
    assert "dont_log_this_method" not in s.getvalue()

    s.seek(0)

    found = []
    for v in iter_decoded_log_format(s):
        if v["message_type"] == "KA":
            found.append(v)

    assert found == [
        {"message_type": "KA", "argument": "user_password='<redacted>'"},
        {"message_type": "KA", "argument": "arg='<redacted>'"},
        {"argument": "<redacted>", "message_type": "KA"},
    ]
