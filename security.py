import ipaddress
import socket


BLOCKED_HOSTNAMES = {
    "localhost",
    "localhost.localdomain",
}


def is_safe_domain(domain):

    domain = domain.strip().lower()

    if domain in BLOCKED_HOSTNAMES:
        return False

    if domain.endswith(".local"):
        return False

    try:
        ip = ipaddress.ip_address(domain)

        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        ):
            return False

    except ValueError:
        pass

    try:
        addresses = socket.getaddrinfo(
            domain,
            443,
            type=socket.SOCK_STREAM
        )

        for address in addresses:

            ip = ipaddress.ip_address(
                address[4][0]
            )

            if (
                ip.is_private
                or ip.is_loopback
                or ip.is_link_local
                or ip.is_reserved
                or ip.is_multicast
            ):
                return False

    except socket.gaierror:
        return False

    return True
