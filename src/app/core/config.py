from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Забота о любимых"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
