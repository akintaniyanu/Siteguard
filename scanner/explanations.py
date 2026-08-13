EXPLANATIONS = {

    "HSTS": {
        "message": (
            "Strict-Transport-Security is missing. "
            "This header helps browsers use HTTPS."
        ),
        "recommendation": (
            "Configure HSTS after ensuring the website "
            "works correctly over HTTPS."
        )
    },

    "CSP": {
        "message": (
            "Content-Security-Policy is missing. "
            "This header can help reduce certain "
            "browser-based attacks."
        ),
        "recommendation": (
            "Configure an appropriate Content-Security-Policy."
        )
    },

    "X-Frame-Options": {
        "message": (
            "X-Frame-Options is missing. "
            "This header can help control framing "
            "of your website."
        ),
        "recommendation": (
            "Configure an appropriate anti-framing policy."
        )
    },

    "SPF": {
        "message": (
            "No SPF record was detected for this domain."
        ),
        "recommendation": (
            "Review your email infrastructure and "
            "configure an appropriate SPF policy."
        )
    },

    "DMARC": {
        "message": (
            "No DMARC record was detected."
        ),
        "recommendation": (
            "Configure DMARC for your domain's email "
            "authentication policy."
        )
    }
}
