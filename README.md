# 🛡️ SiteGuard

## Website Security Scanner

SiteGuard is a beginner-friendly cybersecurity project that checks a website's basic security posture.

The project was built as part of my cybersecurity learning journey, while learning Python, web security, APIs, DNS, TLS, security headers, cookies, SQLite and basic security testing.

---

## Why I Built SiteGuard

I didn't start SiteGuard because I wanted to build another cybersecurity project.

I started because I noticed a simple problem:

Most people visit websites without knowing how secure they actually are.

You see the 🔒 icon in your browser and assume everything is fine.

But what if you could actually check?

Does the website use HTTPS?

Is the SSL/TLS certificate valid?

Are important security headers configured?

Does the domain have SPF and DMARC?

SiteGuard is my attempt to turn those questions into a simple security scanner.

---

## Features

SiteGuard currently includes checks for:

- HTTPS
- TLS certificate
- Security headers
- Cookies
- DNS
- SPF
- DMARC
- Security scoring
- Scan history
- Domain management
- Flask API
- Web dashboard
- Basic SSRF protection
- Error handling

---

## Technology Stack

- Python
- Flask
- Requests
- SQLite
- HTML
- CSS
- JavaScript
- DNS
- TLS/SSL

---

## Project Structure

```text
siteguard/
│
├── app.py
├── database.py
├── security.py
├── requirements.txt
├── SECURITY_TESTING.md
├── README.md
│
├── scanner/
│   └── siteguard.py
│
└── templates/
    └── index.html
