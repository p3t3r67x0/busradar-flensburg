from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from functools import lru_cache

import config



@lru_cache()
def get_settings():
    return config.Settings()


url_base = get_settings().url_base
url_detail = get_settings().url_detail
username = get_settings().username
password = get_settings().password
database = get_settings().database
port = get_settings().port
host = get_settings().host


DATABASE_URL = f'postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}'


Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
