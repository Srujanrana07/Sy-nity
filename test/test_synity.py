from core.identity import IdentityVerifier
from core.system import SystemChecker
from core.trust import TrustEngine

def test_system_check():
    checker = SystemChecker()
    result = checker.check()
    assert "system_ok" in result

def test_identity_error():
    verifier = IdentityVerifier()
    result = verifier.verify("non_existent.jpg")
    assert result["status"] == "error"

def test_trust_engine():
    trust = TrustEngine()
    identity = {"status": "verified", "faces": 1}
    system = {"system_ok": True}
    score = trust.compute(identity, system)
    assert score > 0
