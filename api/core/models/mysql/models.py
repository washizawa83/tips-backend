import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, String, TIMESTAMP
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.sql import func


@as_declarative()
class Base(object):
    id = Column('id', UUIDType(binary=False),
                primary_key=True, default=uuid.uuid4)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    created_at = Column(
        TIMESTAMP, server_default=func.now())
