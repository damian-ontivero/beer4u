from beer4u.beer.beer.application.query.search_all_query import (
    SearchAllBeerQuery,
)
from beer4u.beer.beer.application.query.search_all_query_handler import (
    SearchAllBeerQueryHandler,
)
from beer4u.beer.beer.application.query.search_by_id_query import (
    SearchBeerByIdQuery,
)
from beer4u.beer.beer.application.query.search_by_id_query_handler import (
    SearchBeerByIdQueryHandler,
)
from beer4u.beer.beer.infrastructure.persistence.sqlite.beer_repository import (
    SqliteBeerRepository,
)
from beer4u.shared.infrastructure.bus.query.in_memory_query_bus import (
    InMemoryQueryBus,
)
from beer4u.shared.infrastructure.persistence.sqlite.db import SessionLocal

QUERY_HANDLER_MAPPING = {
    SearchAllBeerQuery: SearchAllBeerQueryHandler(
        SqliteBeerRepository(SessionLocal)
    ),
    SearchBeerByIdQuery: SearchBeerByIdQueryHandler(
        SqliteBeerRepository(SessionLocal)
    ),
}


def register_query_handlers():
    for query, handler in QUERY_HANDLER_MAPPING.items():
        InMemoryQueryBus().register(query, handler)
