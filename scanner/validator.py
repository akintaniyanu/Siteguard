import re


def is_valid_domain(domain):
    pattern = r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$"

    if re.match(pattern, domain):
        return True

    return False


domain = input("Enter a domain: ").strip()

if is_valid_domain(domain):
    print("✅ Valid domain")
else:
    print("❌ Invalid domain")

