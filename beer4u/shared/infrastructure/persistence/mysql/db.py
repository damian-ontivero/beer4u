from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


def get_config():
    """Returns a config parser."""
    config = ConfigParser()
    config.read("beer4u/config.ini")

    return config


def get_session(
    db_user: str,
    db_pass: str,
    db_host: str,
    db_port: int,
    db_name: str,
    db_pool_size: int,
    db_auto_commit: bool,
    db_verbose: bool,
):
    """Returns a mysql session."""

    database_uri = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        db_user, db_pass, db_host, db_port, db_name
    )

    engine = create_engine(
        database_uri, pool_size=db_pool_size, echo=db_verbose
    )

    return sessionmaker(bind=engine, autocommit=db_auto_commit)


config = get_config()

MySqlSession = get_session(
    config.get("database", "user"),
    config.get("database", "pass"),
    config.get("database", "host"),
    config.getint("database", "port"),
    config.get("database", "database"),
    config.getint("database", "pool_size"),
    config.getboolean("database", "autocommit"),
    config.getboolean("database", "verbose"),
)


class Base(DeclarativeBase):
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
