"""Central exception handlers (183)."""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

async def _http(req: Request, exc: Exception) -> JSONResponse:
    status = getattr(exc, "status_code", 500)
    return JSONResponse(status_code=status, content={"detail": str(getattr(exc, 'detail', exc))})

def register_exception_handlers(app: FastAPI) -> None:
    from fastapi import HTTPException
    app.add_exception_handler(HTTPException, _http)
