from beer4u.shared.domain.bus.query import Query, QueryBus, QueryHandler


class InMemoryQueryBus(QueryBus):

    def __init__(self, query_handlers: list[QueryHandler]):
        self._query_handlers = self._handlers = {
            handler.subscribe_to(): handler for handler in query_handlers
        }

    def dispatch(self, query: Query) -> None:
        self._query_handlers.get(type(query)).handle(query)
