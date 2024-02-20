from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


def get_session():
    database_uri = "sqlite:///./database.db"

    engine = create_engine(
        database_uri,
        connect_args={"check_same_thread": False},
    )

    return sessionmaker(bind=engine, autocommit=False, autoflush=False)


SqliteSession = get_session()


class Base(DeclarativeBase):
    pass
