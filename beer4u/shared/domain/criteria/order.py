from .order_by import OrderBy
from .order_type import OrderType


class Order:

    __slots__ = (
        "_order_by",
        "_order_type",
    )

    def __init__(self, order_by: OrderBy, order_type: OrderType) -> None:
        self._order_by = order_by
        self._order_type = order_type

    @property
    def order_by(self) -> str:
        return self._order_by.value

    @property
    def order_type(self) -> str:
        return self._order_type.value

    @property
    def is_none(self) -> bool:
        return self._order_type.is_none

    @staticmethod
    def none() -> "Order":
        return Order(OrderBy(""), OrderType("NONE"))

    @classmethod
    def from_primitives(cls, order_by: str | None, order_type: str) -> "Order":
        if order_by is None:
            return cls.none()
        return cls(OrderBy(order_by), OrderType(order_type))

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
