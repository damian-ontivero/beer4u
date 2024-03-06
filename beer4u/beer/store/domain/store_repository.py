from abc import ABCMeta, abstractmethod

from beer4u.shared.domain.criteria import Criteria

from .store import Store

FILTER_OPERATOR_MAPPER = {
    "eq": lambda m, k, v: getattr(m, k) == v,
    "gt": lambda m, k, v: getattr(m, k) > v,
    "ge": lambda m, k, v: getattr(m, k) >= v,
    "lt": lambda m, k, v: getattr(m, k) < v,
    "le": lambda m, k, v: getattr(m, k) <= v,
    "in": lambda m, k, v: getattr(m, k).in_(v.split(",")),
    "btw": lambda m, k, v: getattr(m, k).between(*v.split(",")),
    "lk": lambda m, k, v: getattr(m, k).ilike(f"%{v}%"),
}


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
