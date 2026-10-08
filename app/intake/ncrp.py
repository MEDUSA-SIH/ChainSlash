"""Phase 17 stub core: UPI vault hash only. Join logic lives in ext/upi_link (EXT_ENABLED)."""
import hashlib

def hash_vpa(vpa_norm: str, kms_salt: str) -> str:
    return hashlib.sha256((kms_salt + vpa_norm).encode()).hexdigest()
