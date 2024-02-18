from beer4u.shared.domain.bus.query.query import Query
from beer4u.shared.domain.bus.query.query_handler import QueryHandler


class InMemoryQueryBus:

    _instance = None

    def __new__(cls) -> "InMemoryQueryBus":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._handlers = {}
        return cls._instance

    def register(self, query: Query, handler: QueryHandler) -> None:
        if not issubclass(query, Query):
            raise TypeError(
                "Invalid query type: {c}. Expected: Query".format(
                    c=query.__class__.__name__
                )
            )
        if not isinstance(handler, QueryHandler):
            raise TypeError(
                "Invalid handler type: {c}. Expected: QueryHandler".format(
                    c=handler.__class__.__name__
                )
            )
        if type(query) in self._handlers:
            raise NotImplementedError(
                f"Query {type(query)} is already registered"
            )
        self._handlers[query] = handler

    def ask(self, query: Query):
        if not isinstance(query, Query):
            raise TypeError(
                "Invalid query type: {c}. Expected: Query".format(
                    c=query.__class__.__name__
                )
            )
        if type(query) not in self._handlers:
            raise NotImplementedError(
                "No registered handler found for query: {c}".format(
                    c=query.__class__.__name__
                )
            )
        handler = self._handlers[type(query)]
        return handler.handle(query)
