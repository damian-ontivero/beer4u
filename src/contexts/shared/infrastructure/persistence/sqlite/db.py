from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class SQLiteDB:

    @staticmethod
    def create_session(
        db_uri: str,
        db_autocommit: bool,
        db_verbose: bool,
    ):
        engine = create_engine(
            db_uri,
            connect_args={"check_same_thread": False},
            echo=db_verbose,
        )

        return sessionmaker(bind=engine, autocommit=db_autocommit)


class Base(DeclarativeBase):
    pass
