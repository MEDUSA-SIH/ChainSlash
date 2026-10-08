"""Phase 6 Neo4j client stub."""
from app.config import settings

def get_driver():
    return {"uri": settings.NEO4J_URI}
