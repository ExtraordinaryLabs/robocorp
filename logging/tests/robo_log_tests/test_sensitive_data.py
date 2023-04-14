import robo_log


def test_sensitive_data():
    from imp import reload
    from robo_log_tests._resources import check_sensitive_data
    from io import StringIO
    from robo_log import iter_decoded_log_format_from_stream

    s = StringIO()

    def write(msg):
        s.write(msg)

    with robo_log.setup_auto_logging():
        check_sensitive_data = reload(check_sensitive_data)

        with robo_log.add_in_memory_log_output(write):
            check_sensitive_data.run()

    assert "my_pass" not in s.getvalue()
    assert "this should not be shown" not in s.getvalue()
    assert "dont_log_this_arg" not in s.getvalue()
    assert "dont_log_this_method" not in s.getvalue()

    s.seek(0)

    found = []
    for v in iter_decoded_log_format_from_stream(s):
        if v["message_type"] == "EA":
            found.append(v)

    assert found == [
        {"message_type": "EA", "name": "user_password", "value": "'<redacted>'"},
        {"message_type": "EA", "name": "arg", "value": "'<redacted>'"},
        {"message_type": "EA", "name": "some_arg", "value": "<redacted>"},
    ]
