from abc import ABCMeta, abstractmethod

from .query import Query


class QueryBus(metaclass=ABCMeta):

    @abstractmethod
    def ask(self, query: Query):
        raise NotImplementedError


class QueryNotRegisteredError(Exception):

    def __init__(self, query: Query):
        super().__init__(f"No handler for {query.__class__.__name__}")
