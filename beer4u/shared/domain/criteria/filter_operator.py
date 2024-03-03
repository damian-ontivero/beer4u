class FilterOperator:

    __slots__ = ("_value",)

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    IS_ANY_OF = "IS_ANY_OF"
    IS_NOT_ANY_OF = "IS_NOT_ANY_OF"
    IS_EMPTY = "IS_EMPTY"
    IS_NOT_EMPTY = "IS_NOT_EMPTY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"

    def __init__(self, value: str) -> None:
        if value not in (
            FilterOperator.EQUALS,
            FilterOperator.NOT_EQUALS,
            FilterOperator.CONTAINS,
            FilterOperator.NOT_CONTAINS,
            FilterOperator.IS_ANY_OF,
            FilterOperator.IS_NOT_ANY_OF,
            FilterOperator.IS_EMPTY,
            FilterOperator.IS_NOT_EMPTY,
            FilterOperator.STARTS_WITH,
            FilterOperator.ENDS_WITH,
            FilterOperator.GT,
            FilterOperator.GE,
            FilterOperator.LT,
            FilterOperator.LE,
        ):
            raise ValueError("Invalid filter operator")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FilterOperator):
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
