from sqlalchemy import Boolean, Column, Float, String

from beer4u.shared.infrastructure.persistence.sqlite.db import Base


class BeerSqliteModel(Base):
    __tablename__ = "beer"

    id = Column(String(32), primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    type = Column(String(100))
    alcohol = Column(Float)
    description = Column(String(255))
    discarded = Column(Boolean)
