from .filter import Filter


class Filters:

    def __init__(self, conjunction: str, filter_list: list[Filter]):
        if conjunction not in ["AND", "OR"]:
            raise ValueError("Conjunction must be 'AND' or 'OR'")
        if not all(isinstance(filter, Filter) for filter in filter_list):
            raise TypeError("Filter list must be a list of Filter")
        self._conjunction = conjunction
        self._filter_list = filter_list

    @property
    def conjunction(self) -> str:
        return self._conjunction

    @property
    def filter_list(self) -> list[Filter]:
        return self._filter_list

    @property
    def is_empty(self) -> bool:
        return len(self._filter_list) == 0

    @classmethod
    def from_primitives(cls, conjunction: str, filter_list: list) -> "Filters":
        return cls(
            conjunction=conjunction,
            filter_list=[
                Filter.from_primitives(**filter) for filter in filter_list
            ],
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Filters):
            return NotImplemented
        return (
            self._conjunction == other._conjunction
            and self._filter_list == other._filter_list
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._conjunction, self._filter_list))

    def __repr__(self) -> str:
        return (
            "{c}(conjunction={conjunction!r}, filter_list={filter_list!r})"
        ).format(
            c=self.__class__.__name__,
            conjunction=self._conjunction,
            filter_list=self._filter_list,
        )
