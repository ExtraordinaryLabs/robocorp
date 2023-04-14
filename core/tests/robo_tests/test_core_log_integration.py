from robo_tests.fixtures import robo_run


def test_core_log_integration_error_in_import(datadir):
    from robo_log import verify_log_messages_from_log_html

    result = robo_run(
        ["run", "main_with_error_in_import.py"], returncode=1, cwd=str(datadir)
    )

    decoded = result.stderr.decode("utf-8", "replace")
    assert (
        "ModuleNotFoundError: No module named 'module_that_does_not_exist'" in decoded
    )
    decoded = result.stdout.decode("utf-8", "replace")

    log_target = datadir / "output" / "log.html"
    assert log_target.exists()

    msgs = verify_log_messages_from_log_html(
        log_target,
        [
            {
                "message_type": "STB",
                "message": "ModuleNotFoundError: No module named 'module_that_does_not_exist'",
            },
            # Note: the setup is a task which doesn't have a suite!
            {
                "message_type": "ST",
                "name": "Setup",
                "suite_id": "setup",
                "lineno": 0,
            },
            {
                "message_type": "ET",
                "status": "ERROR",
                "message": "No module named 'module_that_does_not_exist'",
            },
        ],
    )

    if False:  # Manually debugging
        for m in msgs:
            print(m)

        import webbrowser

        webbrowser.open(log_target.as_uri())


def test_core_log_integration_config_log(datadir):
    from robo_log import verify_log_messages_from_log_html

    result = robo_run(["run", "simple.py"], returncode=0, cwd=str(datadir))

    decoded = result.stderr.decode("utf-8", "replace")
    print(decoded)
    decoded = result.stdout.decode("utf-8", "replace")
    print(decoded)

    log_target = datadir / "output" / "log.html"
    assert log_target.exists()

    msgs = verify_log_messages_from_log_html(
        log_target,
        [],
    )

    if False:  # Manually debugging
        for m in msgs:
            print(m)

        import webbrowser

        webbrowser.open(log_target.as_uri())
