"""Phase 26 pydantic-settings. .env never committed."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEMO_MODE: bool = True
    EXT_ENABLED: bool = False
    SECRET_KEY: str = "change-me"
    POSTGRES_USER: str = "sih"
    REDIS_URL: str = "redis://redis:6379/0"
    NEO4J_URI: str = "bolt://neo4j:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "sih26183"
    ATTRIBUTION_MAX_HOPS: int = 5
    BRIDGE_DECAY: float = 0.8
    KMS_SALT_VERSION: int = 1

    class Config:
        env_file = ".env"

settings = Settings()
