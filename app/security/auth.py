"""Phase 22 compat shim — real logic lives in app.core.security (183-native)."""
from app.core.security import Investigator, hash_password, verify_password, create_access_token, decode_access_token, require_role, require_case_access, require_mfa

def check_role(user: dict, required: str) -> bool:
    return user.get("role") == required or user.get("role") == "admin"
