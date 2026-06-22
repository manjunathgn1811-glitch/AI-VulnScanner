def risk_analysis(services):

    score = 0

    for service in services:

        if service["service"] in ["FTP","TELNET"]:
            score += 3

        elif service["service"] in ["HTTP"]:
            score += 1

    if score >= 5:
        return "HIGH"

    elif score >= 2:
        return "MEDIUM"

    return "LOW"