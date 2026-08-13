import requests

domain = input("Enter a domain: ").strip()

url = "https://" + domain

try:
    response = requests.get(url, timeout=10)

    print("✅ Website is reachable")
    print("Status:", response.status_code)

except requests.exceptions.RequestException:
    print("❌ Could not reach the website")
