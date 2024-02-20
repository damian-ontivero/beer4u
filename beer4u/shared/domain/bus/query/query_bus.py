from abc import ABCMeta, abstractmethod

from .query import Query
from .query_handler import QueryHandler


class QueryBus(metaclass=ABCMeta):

    @abstractmethod
    def register(self, query: Query, handler: QueryHandler) -> None:
        raise NotImplementedError

    @abstractmethod
    def ask(self, query: Query):
        raise NotImplementedError
