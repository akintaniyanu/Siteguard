import dns.resolver


def check_dmarc(domain):

    dmarc_domain = "_dmarc." + domain

    try:
        answers = dns.resolver.resolve(dmarc_domain, "TXT")

        for answer in answers:

            record = str(answer)

            if "v=DMARC1" in record.upper():

                print("DMARC: ✅ Found")
                print("Record:", record)

                if "p=reject" in record.lower():
                    print("Policy: REJECT")

                elif "p=quarantine" in record.lower():
                    print("Policy: QUARANTINE")

                elif "p=none" in record.lower():
                    print("Policy: NONE")

                return True

        print("DMARC: ❌ Not found")
        return False

    except Exception:
        print("DMARC: ❌ Not found")

        return False


domain = input("Enter a domain: ").strip()

check_dmarc(domain)
