import requests


def check_https(domain):
    url = "https://" + domain

    try:
        response = requests.get(url, timeout=10)

        print("HTTPS: ✅")
        print("Status:", response.status_code)

    except requests.exceptions.SSLError:
        print("HTTPS: ❌")
        print("SSL/TLS certificate problem")

    except requests.exceptions.RequestException:
        print("HTTPS: ❌")
        print("Could not connect using HTTPS")


domain = input("Enter a domain: ").strip()

check_https(domain)
