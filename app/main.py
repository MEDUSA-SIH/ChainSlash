"""Phase 7 gateway (183) + Phase 26 config. DEMO_MODE=true runs offline with same engine paths."""
from __future__ import annotations
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.config import get_settings

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    app.state.settings = settings
    app.state.db_engine = None
    app.state.redis = None
    try:
        yield
    finally:
        eng = getattr(app.state, "db_engine", None)
        if eng is not None and hasattr(eng, "dispose"):
            await eng.dispose()

def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="ChainX SIH26183 VASP Tracer", version=settings.APP_VERSION, lifespan=lifespan)
    app.state.settings = settings
    origins = [o.strip() for o in settings.CORS_ALLOW_ORIGINS.split(",")]
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.include_router(router)
    return app

app = create_app()
