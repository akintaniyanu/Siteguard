class CheckResult:

    def __init__(
        self,
        name,
        status,
        severity,
        message,
        recommendation
    ):
        self.name = name
        self.status = status
        self.severity = severity
        self.message = message
        self.recommendation = recommendation

    def to_dict(self):

        return {
            "name": self.name,
            "status": self.status,
            "severity": self.severity,
            "message": self.message,
            "recommendation": self.recommendation
        }
