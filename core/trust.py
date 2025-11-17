class TrustEngine:
    def compute(self, identity_result, system_result):
        if identity_result["status"] != "verified":
            return 0.0

        score = 0.5  # Base score if a face is detected

        # Reward more faces detected (not common but just logic)
        score += min(identity_result["faces"] * 0.1, 0.3)

        # Reduce score if system resources are overloaded
        if not system_result["system_ok"]:
            score -= 0.4

        return max(0.0, min(score, 1.0))
