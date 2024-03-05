from .order import Order


class Orders:

    def __init__(self, order_list: list[Order]):
        if not all(isinstance(order, Order) for order in order_list):
            raise TypeError("Order list must be a list of Order")
        self._order_list = order_list

    @property
    def order_list(self) -> list[Order]:
        return self._order_list

    @property
    def is_empty(self) -> bool:
        return len(self._order_list) == 0

    @classmethod
    def from_primitives(cls, order_list: list) -> "Orders":
        return cls(
            order_list=[Order.from_primitives(**order) for order in order_list]
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Orders):
            return NotImplemented
        return self._order_list == other._order_list

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._order_list)

    def __repr__(self) -> str:
        return "{c}(order_list={order_list!r})".format(
            c=self.__class__.__name__,
            order_list=self._order_list,
        )
