from sqlalchemy import create_engine

from api.features.tips.data.models.tips import Tip
from api.features.tips.data.models.tags import Tag
from api.features.tips.data.models.tags_relation import tag_relation
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql+pymysql://root@db:3306/tips?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Tip.metadata.drop_all(bind=engine)
    Tag.metadata.drop_all(bind=engine)
    tag_relation.metadata.drop_all(bind=engine)
    Tip.metadata.create_all(bind=engine)
    Tag.metadata.create_all(bind=engine)
    tag_relation.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
