import dns.resolver


def check_spf(domain):

    try:
        answers = dns.resolver.resolve(domain, "TXT")

        for answer in answers:

            record = str(answer)

            if "v=spf1" in record.lower():

                print("SPF: ✅ Found")
                print("Record:", record)

                return True

        print("SPF: ❌ Not found")
        return False

    except Exception:
        print("SPF: ❌ Could not check")

        return False


domain = input("Enter a domain: ").strip()

check_spf(domain)
