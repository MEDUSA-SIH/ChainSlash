"""Phase 26 pydantic-settings (183). .env never committed."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    APP_VERSION: str = "0.1.0"
    DEMO_MODE: bool = True
    EXT_ENABLED: bool = False
    SECRET_KEY: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES_MINUTES: int = 60
    POSTGRES_USER: str = "sih"
    POSTGRES_PASSWORD: str = "sih26183"
    POSTGRES_DB: str = "sih26183"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    REDIS_URL: str = "redis://redis:6379/0"
    REDIS_HOST: str = "redis"
    NEO4J_URI: str = "bolt://neo4j:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "sih26183"
    ATTRIBUTION_MAX_HOPS: int = 5
    BRIDGE_DECAY: float = 0.8
    KMS_SALT_VERSION: int = 1
    PROVIDER_TRON_ENABLED: bool = True
    PROVIDER_ETH_ENABLED: bool = True
    PROVIDER_BNB_ENABLED: bool = True
    PROVIDER_SOL_ENABLED: bool = True
    PROVIDER_POL_ENABLED: bool = True
    PROVIDER_BTC_ENABLED: bool = True
    SAHYOG_ENDPOINT: str = ""
    NCRP_ENDPOINT: str = ""
    CORS_ALLOW_ORIGINS: str = "*"

settings = Settings()

def get_settings() -> Settings:
    return settings
