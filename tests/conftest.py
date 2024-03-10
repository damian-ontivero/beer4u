import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.contexts.shared.infrastructure.persistence.sqlite.db import Base

engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    import src.contexts.beer.beer.infrastructure.persistence.sqlite
    import src.contexts.beer.store.infrastructure.persistence.sqlite
    from src.contexts.shared.infrastructure.persistence.sqlite.db import Base

    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def mock_beer_repository():
    from src.contexts.beer.beer.infrastructure.persistence.sqlite import (
        SqliteBeerRepository,
    )

    return SqliteBeerRepository(SessionLocal)


@pytest.fixture(scope="function")
def mock_store_repository():
    from src.contexts.beer.store.infrastructure.persistence.sqlite import (
        SqliteStoreRepository,
    )

    return SqliteStoreRepository(SessionLocal)
