import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from beer4u.shared.infrastructure.persistence.sqlite.db import Base

engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    import beer4u.beer.beer.infrastructure.persistence.sqlite
    import beer4u.beer.store.infrastructure.persistence.sqlite
    from beer4u.shared.infrastructure.persistence.sqlite.db import Base

    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def mock_beer_repository():
    from beer4u.beer.beer.infrastructure.persistence.sqlite import (
        SqliteBeerRepository,
    )

    return SqliteBeerRepository(SessionLocal)


@pytest.fixture(scope="function")
def mock_store_repository():
    from beer4u.beer.store.infrastructure.persistence.sqlite import (
        SqliteStoreRepository,
    )

    return SqliteStoreRepository(SessionLocal)
