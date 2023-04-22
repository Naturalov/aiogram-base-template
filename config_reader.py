from typing import Optional

from pydantic import BaseSettings, SecretStr, validator, BaseModel


class Settings(BaseSettings):
    bot_token: Optional[str]

    DATABASE_DNS: Optional[str] = "sqlite://db.sqlite"

    #
    # @validator("fsm_mode")
    # def fsm_type_check(cls, v):
    #     if v not in ("memory", "redis"):
    #         raise ValueError("Incorrect fsm_mode. Must be one of: memory, redis")
    #     return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = Settings()
