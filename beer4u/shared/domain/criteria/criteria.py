from .filters import Filters
from .orders import Orders


class Criteria:

    __slots__ = (
        "_filters",
        "_orders",
        "_page_size",
        "_page_number",
    )

    def __init__(
        self,
        filters: Filters | None,
        orders: Orders | None,
        page_size: int | None,
        page_number: int | None,
    ):
        if filters is not None:
            if not isinstance(filters, Filters):
                raise TypeError("Filters must be a Filters")
        if orders is not None:
            if not isinstance(orders, Orders):
                raise TypeError("Orders must be a Orders")
        if page_size is not None:
            if not isinstance(page_size, int):
                raise TypeError("Page size must be an integer")
            if page_size < 1:
                raise ValueError("Page size must be greater than 0")
        if page_number is not None:
            if not isinstance(page_number, int):
                raise TypeError("Page number must be an integer")
            if page_number < 1:
                raise ValueError("Page number must be greater than 0")
        self._filters = filters
        self._orders = orders
        self._page_size = page_size
        self._page_number = page_number

    @property
    def filters(self) -> Filters | None:
        return self._filters

    @property
    def orders(self) -> Orders | None:
        return self._orders

    @property
    def page_size(self) -> int | None:
        return self._page_size

    @property
    def page_number(self) -> int | None:
        return self._page_number

    @property
    def has_filters(self) -> bool:
        if self._filters is not None:
            return not self._filters.is_empty

    @property
    def has_orders(self) -> bool:
        if self._orders is not None:
            return not self._orders.is_empty

    @classmethod
    def from_primitives(
        cls,
        filters: dict | None,
        orders: list | None,
        page_size: int | None,
        page_number: int | None,
    ) -> "Criteria":
        if filters is not None:
            filters = Filters.from_primitives(**filters)
        if orders is not None:
            orders = Orders.from_primitives(orders)
        return cls(filters, orders, page_size, page_number)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Criteria):
            return NotImplemented
        return (
            self._filters == other.filters
            and self._orders == other.orders
            and self._page_size == other.page_size
            and self._page_number == other.page_number
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                self._filters,
                self._orders,
                self._page_size,
                self._page_number,
            )
        )

    def __repr__(self) -> str:
        return (
            "{c}(filters={filters!r}, orders={orders!r}, "
            "page_size={page_size!r}, page_number={page_number!r})"
        ).format(
            c=self.__class__.__name__,
            filters=self._filters,
            orders=self._orders,
            page_size=self._page_size,
            page_number=self._page_number,
        )
