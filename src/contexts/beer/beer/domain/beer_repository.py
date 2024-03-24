from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .beer import Beer


class BeerRepository(metaclass=ABCMeta):

    @abstractmethod
    def search_all(self) -> list[Beer]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Beer | None:
        raise NotImplementedError

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Beer]:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Beer) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
