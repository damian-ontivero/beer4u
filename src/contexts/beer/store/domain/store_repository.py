from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain.criteria import Criteria

from .store import Store


class StoreRepository(metaclass=ABCMeta):
    """
    Interface for Store repositories.
    This interface should be implemented by any repository
    that is going to be used to retrieve and persist Store instances.
    """

    @abstractmethod
    def search_by_criteria(self, criteria: Criteria) -> list[Store]:
        raise NotImplementedError

    @abstractmethod
    def search_all(self) -> list[Store]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Store | None:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Store) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
