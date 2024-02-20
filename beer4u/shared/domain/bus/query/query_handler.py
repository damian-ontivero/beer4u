from abc import ABCMeta, abstractmethod

from .query import Query


class QueryHandler(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError
