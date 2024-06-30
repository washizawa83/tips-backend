from typing import Iterator
import uuid
import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from api.features.tips.data.models.tables import Tag, Tip


DB_URL = "mysql+pymysql://root@db:3306/tips?charset=utf8"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_session() -> Iterator[Session]:
    session = SessionLocal()

    # データ取得SQL
    # SELECT * FROM tips WHERE JSON_SEARCH(text, 'all', '%example%') IS NOT NULL
    # json_text = json.dumps({
    #     "title": "Example Title",
    #     "content": "This is the content of the tip",
    #     "additional_info": {
    #         "source": "example.com",
    #         "notes": "This is a note"
    #     }
    # })

    # tag = Tag(name='tag01')
    # tips = Tip(user_id='user01',
    #            text=json_text, good=5, is_public=True, tags=[tag])

    # session.add(tips)
    # session.commit()
    try:
        yield session
    finally:
        session.close()
