from typing import Iterator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session


ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/tips?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


def get_session() -> Iterator[Session]:
    db = async_session()
    try:
        yield fb
    finally:
        db.close()
