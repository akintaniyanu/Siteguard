import re
import requests
import socket
import ssl
from datetime import datetime


def is_valid_domain(domain):
    pattern = r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$"
    return bool(re.match(pattern, domain))


def check_https(domain):
    url = "https://" + domain

    try:
        response = requests.get(url, timeout=10)

        print("\nHTTPS: ✅")
        print("Status:", response.status_code)

        return True

    except requests.exceptions.RequestException:
        print("\nHTTPS: ❌")

        return False


def check_certificate(domain):
    context = ssl.create_default_context()

    try:
        with socket.create_connection(
            (domain, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as secure_sock:

                certificate = secure_sock.getpeercert()

                expires = certificate["notAfter"]

                expiry_date = datetime.strptime(
                    expires,
                    "%b %d %H:%M:%S %Y %Z"
                )

                print("Certificate: ✅ Valid")
                print("Expires:", expiry_date)

                return True

    except Exception:
        print("Certificate: ❌ Problem detected")

        return False


def check_headers(domain):
    url = "https://" + domain

    security_headers = {
        "Strict-Transport-Security": "HSTS",
        "Content-Security-Policy": "CSP",
        "X-Frame-Options": "X-Frame-Options"
    }

    try:
        response = requests.get(
            url,
            timeout=10
        )

        print("\nSecurity Headers")
        print("----------------")

        for header, name in security_headers.items():

            if header in response.headers:
                print(f"{name}: ✅")

            else:
                print(f"{name}: ❌")

    except requests.exceptions.RequestException:
        print("Could not check headers")


def check_cookies(domain):
    url = "https://" + domain

    try:
        response = requests.get(
            url,
            timeout=10
        )

        print("\nCookies")
        print("-------")

        if not response.cookies:
            print("No cookies found.")

            return

        for cookie in response.cookies:

            print("Cookie:", cookie.name)

            print(
                "Secure:",
                "✅" if cookie.secure else "❌"
            )

    except requests.exceptions.RequestException:
        print("Could not check cookies")


# ==============================
# MAIN PROGRAM
# ==============================

domain = input("Enter a domain: ").strip()


if not is_valid_domain(domain):

    print()
    print("❌ Invalid domain")
    print("Please enter a domain such as: example.com")


else:

    print()
    print("================================")
    print("          SITEGUARD")
    print("================================")

    print()
    print("Website:", domain)

    print()
    print("--------------------------------")
    print("SECURITY CHECKS")
    print("--------------------------------")

    check_https(domain)

    check_certificate(domain)

    check_headers(domain)

    check_cookies(domain)

    print()
    print("--------------------------------")
    print("SCAN COMPLETE")
    print("--------------------------------")
