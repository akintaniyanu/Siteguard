import requests


def explain_error(error):

    if isinstance(
        error,
        requests.exceptions.Timeout
    ):
        return "Connection timeout"

    if isinstance(
        error,
        requests.exceptions.ConnectionError
    ):
        return "Could not connect to website"

    if isinstance(
        error,
        requests.exceptions.SSLError
    ):
        return "SSL/TLS error"

    return "Unexpected error"
