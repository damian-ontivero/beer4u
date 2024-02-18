from beer4u.beer.store.application.query.search_all_query import (
    SearchAllStoreQuery,
)
from beer4u.beer.store.application.query.search_all_query_handler import (
    SearchAllStoreQueryHandler,
)
from beer4u.beer.store.application.query.search_by_id_query import (
    SearchStoreByIdQuery,
)
from beer4u.beer.store.application.query.search_by_id_query_handler import (
    SearchStoreByIdQueryHandler,
)
from beer4u.beer.store.infrastructure.persistence.sqlite.store_repository import (
    SqliteStoreRepository,
)
from beer4u.shared.infrastructure.bus.query.in_memory_query_bus import (
    InMemoryQueryBus,
)
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
