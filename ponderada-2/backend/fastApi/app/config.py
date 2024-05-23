import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = 'sqlite:///database.db'
    


settings = Settings()
