class OrderDirection:

    __slots__ = ("_value",)

    ASC = "ASC"
    DESC = "DESC"
    NONE = "NONE"

    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Order direction must be a string")
        if not len(value) > 0:
            raise ValueError("Order direction cannot be empty")
        if value not in [
            OrderDirection.ASC,
            OrderDirection.DESC,
            OrderDirection.NONE,
        ]:
            raise ValueError("Invalid order direction")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @property
    def is_none(self) -> bool:
        return self._value == OrderDirection.NONE

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderDirection):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(
            c=self.__class__.__name__, value=self._value
        )
