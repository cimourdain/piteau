import re
import subprocess
from datetime import datetime


def test_samples():
    cmd = ["scripts/integration.sh", "PYTHONPATH=. poetry run python"]
    subprocess.Popen(cmd).wait()
    hello_found = False
    ask_time_found = False
    time_response_found = False
    with open("client.log", "r") as f:
        for line in f:

            if not hello_found:
                if re.search(
                    r"Message received from server {\"from\": \"\w*\", \"message\": \"hello test\"}",  # noqa
                    line,
                ):
                    hello_found = True
            elif not ask_time_found:
                if re.search(
                    r"Message received from server {\"from\": \"\w*\", \"message\": \"/time please\"}",  # noqa
                    line,
                ):
                    ask_time_found = True
            elif not time_response_found:
                print(line)
                regex_result = re.search(
                    r"Message received from server {\"from\": \"\w*\", \"message\": \"(\S+)\"}",  # noqa
                    line,
                )
                if regex_result:
                    potential_date = regex_result.group(1)
                    try:
                        datetime.strptime(potential_date, "%Y-%m-%dT%H:%M:%S.%f")
                        time_response_found = True
                    except ValueError:
                        pass

    assert hello_found is True
    assert ask_time_found is True
    assert time_response_found is True

    subprocess.Popen(["rm", "-f", "client.log"])
