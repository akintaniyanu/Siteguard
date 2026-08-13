from https_check import check_https
from certificate import check_certificate
from headers import check_headers
from cookies import check_cookies
from dns_check import check_dns
from spf import check_spf
from dmarc import check_dmarc


def scan(domain):

    print("\n==========================")
    print("       SITEGUARD")
    print("==========================")

    print("\nTarget:", domain)

    print("\n[1] HTTPS")
    check_https(domain)

    print("\n[2] TLS Certificate")
    check_certificate(domain)

    print("\n[3] Security Headers")
    check_headers(domain)

    print("\n[4] Cookies")
    check_cookies(domain)

    print("\n[5] DNS")
    check_dns(domain)

    print("\n[6] SPF")
    check_spf(domain)

    print("\n[7] DMARC")
    check_dmarc(domain)

    print("\n==========================")
    print("       SCAN COMPLETE")
    print("==========================")


if __name__ == "__main__":

    domain = input("Enter a domain: ").strip()

    scan(domain)
