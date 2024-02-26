from beer4u.shared.domain.bus.query import (
    Query,
    QueryBus,
    QueryHandler,
    QueryNotRegisteredError,
)


class InMemoryQueryBus(QueryBus):

    def __init__(self, query_handler_map: dict[Query, QueryHandler]) -> None:
        self._query_handler_map = query_handler_map

    def ask(self, query: Query):
        handler = self._query_handler_map.get(type(query))
        if handler is None:
            raise QueryNotRegisteredError(query)
        return handler.handle(query)
