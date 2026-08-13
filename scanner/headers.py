import requests


SECURITY_HEADERS = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Frame-Options": "X-Frame-Options"
}


def check_headers(domain):
    url = "https://" + domain

    try:
        response = requests.get(url, timeout=10)

        print("\nSecurity Headers")
        print("----------------")

        for header, name in SECURITY_HEADERS.items():

            if header in response.headers:
                print(f"{name}: ✅")
            else:
                print(f"{name}: ❌")

    except requests.exceptions.RequestException:
        print("❌ Could not connect to website")


domain = input("Enter a domain: ").strip()

check_headers(domain)
