import dns.resolver


def check_dns(domain):
    print("\nDNS Records")
    print("-----------")

    record_types = ["A", "AAAA", "MX", "NS", "TXT"]

    for record_type in record_types:

        try:
            answers = dns.resolver.resolve(domain, record_type)

            print(f"\n{record_type}:")

            for answer in answers:
                print(" ", answer)

        except Exception:
            print(f"\n{record_type}: Not found")


domain = input("Enter a domain: ").strip()

check_dns(domain)
