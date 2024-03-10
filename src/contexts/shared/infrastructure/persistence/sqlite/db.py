from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


def get_config():
    """Returns a config parser."""
    config = ConfigParser()
    config.read("beer4u/config.ini")

    return config


def get_session(
    db_autocommit: bool,
    db_verbose: bool,
):
    database_uri = "sqlite:///./database.db"

    engine = create_engine(
        database_uri,
        connect_args={"check_same_thread": False},
        echo=db_verbose,
    )

    return sessionmaker(bind=engine, autocommit=db_autocommit)


config = get_config()

SqliteSession = get_session(
    config.getboolean("database", "autocommit"),
    config.getboolean("database", "verbose"),
)


class Base(DeclarativeBase):
    pass
