import socket
import ssl
from datetime import datetime


def check_certificate(domain):
    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:

                certificate = secure_sock.getpeercert()

                expires = certificate["notAfter"]

                expiry_date = datetime.strptime(
                    expires,
                    "%b %d %H:%M:%S %Y %Z"
                )

                print("Certificate: ✅ Valid")
                print("Expires:", expiry_date)

                print("Domain matches: ✅")

    except ssl.SSLCertVerificationError:
        print("Certificate: ❌ Invalid or untrusted")

    except Exception as error:
        print("Certificate check failed")
        print("Reason:", error)


domain = input("Enter a domain: ").strip()

check_certificate(domain)
