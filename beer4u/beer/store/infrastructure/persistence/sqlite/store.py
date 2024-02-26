from sqlalchemy import JSON, Boolean, Column, String

from beer4u.shared.infrastructure.persistence.sqlite.db import Base


class StoreSqliteModel(Base):
    __tablename__ = "store"

    id = Column(String(32), primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    address = Column(JSON)
    phone = Column(String(15))
    discarded = Column(Boolean)
