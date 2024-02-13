from abc import ABCMeta, abstractmethod

from beer4u.shared.domain.bus.query.query import Query


class QueryHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, query: Query):
        raise NotImplementedError
