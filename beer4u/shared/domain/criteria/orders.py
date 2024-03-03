from .order import Order


class Orders:

    __slots__ = ("_value",)

    def __init__(self, value: list[Order]) -> None:
        self._value = value

    @property
    def value(self) -> list[Order]:
        return self._value

    @property
    def is_empty(self) -> bool:
        return len(self._value) == 0

    @classmethod
    def from_primitives(cls, orders: list[dict]) -> "Orders":
        return cls([Order.from_primitives(**order) for order in orders])

    def to_primitives(self) -> list[dict]:
        return [order.to_primitives() for order in self._value]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Orders):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(orders={orders!r})".format(
            c=self.__class__.__name__, orders=self._value
        )
