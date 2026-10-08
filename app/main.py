"""Phase 7 gateway + Phase 26 config. DEMO_MODE=true runs offline with same engine paths."""
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SIH26183 VASP Tracer")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
