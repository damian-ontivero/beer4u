from .filters import Filters
from .orders import Orders


class Criteria:

    def __init__(
        self,
        filters: Filters,
        orders: Orders,
        page_size: int,
        page_number: int,
    ):
        if not isinstance(filters, Filters):
            raise TypeError("Filters must be an instance of Filters")
        if not isinstance(orders, Orders):
            raise TypeError("Orders must be an instance of Orders")
        if not isinstance(page_size, int):
            raise TypeError("Page size must be an integer")
        if not page_size > 0:
            raise ValueError("Page size must be greater than 0")
        if not isinstance(page_number, int):
            raise TypeError("Page number must be an integer")
        if not page_number > 0:
            raise ValueError("Page number must be greater than 0")
        self._filters = filters
        self._orders = orders
        self._page_size = page_size
        self._page_number = page_number

    @property
    def filters(self) -> Filters:
        return self._filters

    @property
    def orders(self) -> Orders:
        return self._orders

    @property
    def page_size(self) -> int:
        return self._page_size

    @property
    def page_number(self) -> int:
        return self._page_number

    @property
    def has_filters(self) -> bool:
        return not self._filters.is_empty

    @property
    def has_orders(self) -> bool:
        return not self._orders.is_empty

    @classmethod
    def from_primitives(
        cls,
        filters: list[dict] | None,
        orders: list[dict] | None,
        page_size: int | None,
        page_number: int | None,
    ) -> "Criteria":
        return cls(
            Filters.from_primitives(filters) if filters else Filters([]),
            Orders.from_primitives(orders) if orders else Orders([]),
            page_size,
            page_number,
        )

    def to_primitives(self) -> dict:
        return {
            "filters": self._filters.to_primitives(),
            "orders": self._orders.to_primitives(),
            "page_size": self._page_size,
            "page_number": self._page_number,
        }
