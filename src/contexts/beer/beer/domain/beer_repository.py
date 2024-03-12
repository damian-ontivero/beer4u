from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .beer import Beer


class BeerRepository(metaclass=ABCMeta):
    """
    Interface for Beer repositories.
    This interface should be implemented by any repository
    that is going to be used to retrieve and persist Beer instances.
    """

    @abstractmethod
    def search_by_criteria(self, criteria: Criteria) -> list[Beer]:
        raise NotImplementedError

    @abstractmethod
    def search_all(self) -> list[Beer]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Beer | None:
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
