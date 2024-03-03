from .filter import Filter


class Filters:

    __slots__ = ("_value",)

    def __init__(self, value: list[Filter]) -> None:
        self._value = value

    @property
    def value(self) -> list[Filter]:
        return self._value

    @property
    def is_empty(self) -> bool:
        return len(self._value) == 0

    @classmethod
    def from_primitives(cls, filters: list[dict]) -> "Filters":
        return cls([Filter.from_primitives(**filter) for filter in filters])

    def to_primitives(self) -> list[dict]:
        return [filter.to_primitives() for filter in self._value]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Filters):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(filters={filters!r})".format(
            c=self.__class__.__name__, filters=self._value
        )
