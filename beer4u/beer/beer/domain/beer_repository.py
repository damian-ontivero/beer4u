from abc import ABCMeta, abstractmethod

from .beer import Beer

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


class BeerRepository(metaclass=ABCMeta):
    """
    Interface for Beer repositories.
    This interface should be implemented by any repository
    that is going to be used to retrieve and persist Beer instances.
    """

    @abstractmethod
    def search_by_criteria(self) -> list[Beer]:
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
