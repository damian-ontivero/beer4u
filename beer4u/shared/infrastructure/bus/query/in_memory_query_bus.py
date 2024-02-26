from beer4u.shared.domain.bus.query import (
    Query,
    QueryBus,
    QueryHandler,
    RegisteredQueryError,
)


class InMemoryQueryBus(QueryBus):

    def __init__(self, query_handler_map: dict[Query, QueryHandler]) -> None:
        self._query_handler_map = query_handler_map

    def ask(self, query: Query):
        handler = self._query_handler_map.get(type(query))
        if handler is None:
            raise RegisteredQueryError(f"Query: {query!r} not registered")
        return handler.handle(query)
