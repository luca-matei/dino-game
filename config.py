from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Dino Game"
    screen_w: int = 1280
    screen_h: int = 720
    fps: int = 60


settings = Settings()
