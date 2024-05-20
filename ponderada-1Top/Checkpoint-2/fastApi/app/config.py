import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # db_url: str = Field(..., env="DATABASE_URL")
    db_url: str = "postgresql://leao09:adm123@localhost:5432/postgres"


settings = Settings()
