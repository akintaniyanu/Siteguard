def calculate_score(results):

    score = 0

    weights = {
        "HTTPS": 20,
        "TLS Certificate": 20,
        "Security Headers": 20,
        "Cookies": 10,
        "DNS": 10,
        "SPF": 10,
        "DMARC": 10
    }

    for result in results:

        if result["status"] == "PASS":

            score += weights.get(result["name"], 0)

    return score
