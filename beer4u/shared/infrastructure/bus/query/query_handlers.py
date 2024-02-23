from beer4u.shared.domain.bus.query import (
    Query,
    QueryHandler,
    QueryNotRegisteredError,
)


class QueryHandlers(dict[Query, QueryHandler]):

    def __init__(self, query_handlers: list[QueryHandler]):
        self._handlers = {
            handler.subscribe_to(): handler for handler in query_handlers
        }

    def get(self, query: Query) -> QueryHandler:
        handler = self._handlers.get(type(query))
        if handler is None:
            raise QueryNotRegisteredError(query)
        return handler
