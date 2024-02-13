from beer4u.shared.infrastructure.bus.query.in_memory_query_bus import (
    InMemoryQueryBus,
)

QUERY_HANDLER_MAPPING = {}


def register_query():
    for query, handler in QUERY_HANDLER_MAPPING.items():
        InMemoryQueryBus().register(query, handler)
