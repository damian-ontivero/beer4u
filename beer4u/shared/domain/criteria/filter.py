from .filter_field import FilterField
from .filter_operator import FilterOperator
from .filter_value import FilterValue


class Filter:

    __slots__ = (
        "_field",
        "_operator",
        "_value",
    )

    def __init__(
        self, field: FilterField, operator: FilterOperator, value: FilterValue
    ) -> None:
        self._field = field
        self._operator = operator
        self._value = value

    @property
    def field(self) -> str:
        return self._field.value

    @property
    def operator(self) -> str:
        return self._operator.value

    @property
    def value(self) -> str:
        return self._value.value

    @classmethod
    def from_primitives(
        cls, field: str, operator: str, value: str
    ) -> "Filter":
        return cls(
            FilterField(field),
            FilterOperator(operator),
            FilterValue(value),
        )

    def to_primitives(self) -> dict:
        return {
            "field": self._field.value,
            "operator": self._operator.value,
            "value": self._value.value,
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Filter):
            return NotImplemented
        return (
            self._field == other._field
            and self._operator == other._operator
            and self._value == other._value
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._field, self._operator, self._value))

    def __repr__(self) -> str:
        return (
            "{c}(field={field!r}, operator={operator!r}, value={value!r})"
        ).format(
            c=self.__class__.__name__,
            field=self._field,
            operator=self._operator,
            value=self._value,
        )
