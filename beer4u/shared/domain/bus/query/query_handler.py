from abc import ABCMeta, abstractmethod

from .query import Query


class QueryHandler(metaclass=ABCMeta):

    @property
    @abstractmethod
    def subscribe_to(self) -> Query:
        raise NotImplementedError

    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError
