from abc import ABCMeta, abstractmethod

from .query import Query


class QueryHandler(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe_to() -> Query:
        raise NotImplementedError

    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError
