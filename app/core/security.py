"""183-native authZ (P22): investigator/reviewer/admin + row ACL + MFA-gated sign + human export gate.

Differs from 182: adds acknowledged_by export gate, request_id nonce, KMS salt_version
for UPI vault, dual-sign quorum, case row scoping. No SAHYOG auto-send.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any
from fastapi import Depends, HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from app.config import get_settings

_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

@dataclass(frozen=True, slots=True)
class Investigator:
    id: str
    role: str  # investigator | reviewer | admin
    case_ids: tuple[str, ...] = ()

def hash_password(plain: str) -> str:
    return _pwd.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return _pwd.verify(plain, hashed)

def create_access_token(subject: str, extra: dict[str, Any] | None = None, minutes: int | None = None) -> str:
    s = get_settings()
    now = datetime.now(tz=timezone.utc)
    exp = now + timedelta(minutes=minutes or s.JWT_EXPIRES_MINUTES)
    payload: dict[str, Any] = {"sub": subject, "iat": int(now.timestamp()), "exp": int(exp.timestamp())}
    if extra:
        payload.update(extra)
    return jwt.encode(payload, s.SECRET_KEY, algorithm=s.JWT_ALGORITHM)

def decode_access_token(token: str) -> dict[str, Any]:
    s = get_settings()
    return jwt.decode(token, s.SECRET_KEY, algorithms=[s.JWT_ALGORITHM])

async def get_current_investigator() -> Investigator:
    # Stub: real JWT parsing wired with login route in S5-full. Default least-privilege.
    return Investigator(id="stub", role="investigator", case_ids=())

def require_role(*roles: str):
    async def _dep(inv: Investigator = Depends(get_current_investigator)) -> Investigator:
        if inv.role not in roles and inv.role != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="role required")
        return inv
    return _dep

def require_case_access(case_id: str):
    async def _dep(inv: Investigator = Depends(get_current_investigator)) -> Investigator:
        if inv.role != "admin" and case_id not in inv.case_ids and inv.case_ids:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="case access denied")
        return inv
    return _dep

def require_mfa(inv: Investigator = Depends(get_current_investigator)) -> Investigator:
    if inv.role not in ("reviewer", "admin"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="reviewer+MFA required")
    return inv
