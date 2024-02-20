from beer4u.beer.beer.application.query import (
    SearchAllBeerQuery,
    SearchAllBeerQueryHandler,
    SearchBeerByIdQuery,
    SearchBeerByIdQueryHandler,
)
from beer4u.beer.beer.infrastructure.persistence.sqlite import (
    SqliteBeerRepository,
)
from beer4u.shared.infrastructure.bus.query import InMemoryQueryBus
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
