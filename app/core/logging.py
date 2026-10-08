"""Structured logging with secret redaction (183 P22)."""
from __future__ import annotations
import logging, sys
from typing import Any
import structlog

REDACT = ("SECRET_KEY", "DATABASE_URL", "NEO4J_PASSWORD", "POSTGRES_PASSWORD", "KMS")

def _redact(_, __, ed: dict[str, Any]) -> dict[str, Any]:
    for k in list(ed.keys()):
        if any(s in str(k).upper() for s in REDACT):
            ed[k] = "***"
    return ed

def configure_logging() -> None:
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
    structlog.configure(processors=[_redact, structlog.processors.add_log_level, structlog.processors.TimeStamper(fmt="iso"), structlog.processors.JSONRenderer()], cache_logger_on_first_use=True)

def get_logger(name: str | None = None):
    return structlog.get_logger(name)
