from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    url_base: str = Field(validation_alias='URL_BASE')
    url_detail: str = Field(validation_alias='URL_DETAIL')
    password: str = Field(validation_alias='DB_PASS')
    username: str = Field(validation_alias='DB_USER')
    database: str = Field(validation_alias='DB_NAME')
    host: str = Field(validation_alias='DB_HOST')
    port: int = Field(validation_alias='DB_PORT')

    model_config = SettingsConfigDict(env_file='.env', populate_by_name=True)
