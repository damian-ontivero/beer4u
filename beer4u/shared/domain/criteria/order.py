from .order_direction import OrderDirection
from .order_field import OrderField


class Order:

    __slots__ = (
        "_field",
        "_direction",
    )

    def __init__(self, field: OrderField, direction: OrderDirection) -> None:
        self._field = field
        self._direction = direction

    @property
    def field(self) -> OrderField:
        return self._field

    @property
    def direction(self) -> OrderDirection:
        return self._direction

    @property
    def is_none(self) -> bool:
        return self._direction.is_none

    @staticmethod
    def none() -> "Order":
        return Order(OrderField(""), OrderDirection("NONE"))

    @classmethod
    def from_primitives(cls, field: str | None, direction: str) -> "Order":
        if field is None:
            return cls.none()
        return cls(OrderField(field), OrderDirection(direction))

    def to_primitives(self) -> dict:
        return {
            "field": self._field.value,
            "direction": self._direction.value,
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Order):
            return NotImplemented
        return (
            self._field == other._field and self._direction == other._direction
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._field, self._direction))

    def __repr__(self) -> str:
        return "{c}(field={field!r}, direction={direction!r})".format(
            c=self.__class__.__name__,
            field=self._field,
            direction=self._direction,
        )
