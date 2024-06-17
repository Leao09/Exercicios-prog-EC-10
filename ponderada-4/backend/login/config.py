import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'sqlite:///database.db'
    


settings = Settings()
