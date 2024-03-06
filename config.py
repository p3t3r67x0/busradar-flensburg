from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    line_1: str = Field(validation_alias='LINE_1')
    line_2: str = Field(validation_alias='LINE_2')
    line_3: str = Field(validation_alias='LINE_3')
    line_4: str = Field(validation_alias='LINE_4')
    line_5: str = Field(validation_alias='LINE_5')
    line_7: str = Field(validation_alias='LINE_7')
    line_8: str = Field(validation_alias='LINE_8')
    line_10: str = Field(validation_alias='LINE_10')
    line_11: str = Field(validation_alias='LINE_11')
    line_12: str = Field(validation_alias='LINE_12')
    line_14: str = Field(validation_alias='LINE_14')

    url_base: str = Field(validation_alias='URL_BASE')
    url_detail: str = Field(validation_alias='URL_DETAIL')

    password: str = Field(validation_alias='DB_PASS')
    username: str = Field(validation_alias='DB_USER')
    database: str = Field(validation_alias='DB_NAME')
    host: str = Field(validation_alias='DB_HOST')
    port: int = Field(validation_alias='DB_PORT')

    model_config = SettingsConfigDict(env_file='.env', populate_by_name=True)
