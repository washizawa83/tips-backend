from typing import Iterator

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from api.features.tips.data.models.tables import Tag, Tip, User
import uuid

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

DB_URL = "mysql+pymysql://root@db:3306/tips?charset=utf8"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_session() -> Iterator[Session]:
    session = SessionLocal()

    # tag = Tag(name='tag01')
    # tips = Tip(user_id='user01',
    #            text='tips text', good=5, is_public=True, tags=[tag])

    # session.add(tips)
    # session.commit()

    # user = User(name='user02', email='user02@mail.com')
    # session.add(user)
    # session.commit()
    try:
        yield session
    finally:
        session.close()
