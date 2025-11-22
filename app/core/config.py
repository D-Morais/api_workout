from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "WorkoutAPI"
    database_url: str = Field(default="sqlite+aiosqlite:///./workout.db")


settings = Settings()
