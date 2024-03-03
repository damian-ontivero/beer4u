from .field import Field
from .order_type import OrderType


class Order:

    __slots__ = (
        "_field",
        "_direction",
    )

    def __init__(self, field: Field, order_type: OrderType) -> None:
        self._field = field
        self._order_type = order_type

    @property
    def is_none(self) -> bool:
        return self._order_type.is_none

    @staticmethod
    def none() -> "Order":
        return Order(Field(""), OrderType("NONE"))

    @classmethod
    def from_primitives(cls, field: str | None, order_type: str) -> "Order":
        if field is None:
            return cls.none()
        return cls(Field(field), OrderType(order_type))

    def to_primitives(self) -> dict:
        return {
            "order_by": self._order_by.value,
            "order_type": self._order_type.value,
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Order):
            return NotImplemented
        return (
            self._order_by == other._order_by
            and self._order_type == other._order_type
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._order_by, self._order_type))

    def __repr__(self) -> str:
        return "{c}(order_by={order_by!r}, order_type={order_type!r})".format(
            c=self.__class__.__name__,
            order_by=self._order_by,
            order_type=self._order_type,
        )
