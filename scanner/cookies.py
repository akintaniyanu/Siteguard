import requests


def check_cookies(domain):
    url = "https://" + domain

    try:
        response = requests.get(url, timeout=10)

        cookies = response.cookies

        if not cookies:
            print("No cookies found in the response.")
            return

        print("\nCookies")
        print("-------")

        for cookie in cookies:

            print("\nCookie:", cookie.name)

            print("Secure:", "✅" if cookie.secure else "❌")

            httponly = "HttpOnly" in cookie._rest.get("HttpOnly", "")

            print("HttpOnly:", "✅" if httponly else "❌")

            print("SameSite: Check response headers")

    except requests.exceptions.RequestException:
        print("❌ Could not connect to website")


domain = input("Enter a domain: ").strip()

check_cookies(domain)
