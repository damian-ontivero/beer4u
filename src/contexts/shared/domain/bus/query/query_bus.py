from abc import ABCMeta, abstractmethod

from .query import Query


class QueryBus(metaclass=ABCMeta):

    @abstractmethod
    def ask(self, query: Query):
        raise NotImplementedError


class RegisteredQueryError(Exception):
    pass
