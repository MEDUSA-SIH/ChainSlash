"""Shared pytest fixtures (183)."""
from __future__ import annotations
import os, sys
from pathlib import Path
import pytest

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

os.environ.setdefault("DEMO_MODE", "true")
os.environ.setdefault("EXT_ENABLED", "false")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("KMS_SALT_VERSION", "1")
