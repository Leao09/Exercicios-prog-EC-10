import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # db_url: str = Field(..., env="DATABASE_URL")
    db_url: str = "postgres://leao09:6FF0Pb6lV3eS2eTpMii4Gblu1T3wgKhL@dpg-cp5gj7v79t8c73ettnh0-a/data_67ec"


settings = Settings()
