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
db_user = config.get("database", "user")
db_pass = config.get("database", "pass")
db_host = config.get("database", "host")
db_port = config.getint("database", "port")
db_name = config.get("database", "database")
db_pool_size = config.getint("database", "pool_size")
db_auto_commit = config.getboolean("database", "autocommit")
db_verbose = config.getboolean("database", "verbose")

SessionLocal = get_session(
    db_user,
    db_pass,
    db_host,
    db_port,
    db_name,
    db_pool_size,
    db_auto_commit,
    db_verbose,
)


class Base(DeclarativeBase):
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
