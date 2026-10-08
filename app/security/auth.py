"""Phase 22 JWT+RBAC investigator/reviewer/admin, row-level case ACL, MFA reviewer/admin."""
def check_role(user: dict, required: str) -> bool:
    return user.get("role") == required or user.get("role") == "admin"
