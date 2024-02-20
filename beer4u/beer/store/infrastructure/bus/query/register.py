from beer4u.beer.store.application.query import (
    SearchAllStoreQuery,
    SearchAllStoreQueryHandler,
    SearchStoreByIdQuery,
    SearchStoreByIdQueryHandler,
)
from beer4u.beer.store.infrastructure.persistence.sqlite import (
    SqliteStoreRepository,
)
from beer4u.shared.infrastructure.bus.query import InMemoryQueryBus
from beer4u.shared.infrastructure.persistence.sqlite.db import SessionLocal

QUERY_HANDLER_MAPPING = {
    SearchAllStoreQuery: SearchAllStoreQueryHandler(
        repository=SqliteStoreRepository(SessionLocal)
    ),
    SearchStoreByIdQuery: SearchStoreByIdQueryHandler(
        repository=SqliteStoreRepository(SessionLocal)
    ),
}


def register_query_handlers():
    for query, handler in QUERY_HANDLER_MAPPING.items():
        InMemoryQueryBus().register(query, handler)
