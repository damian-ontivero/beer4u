from .filter import Filter
from .order import Order


class Criteria:

    __slots__ = (
        "_filters",
        "_orders",
        "_page_size",
        "_page_number",
    )

    def __init__(
        self,
        filters: list[Filter] | None,
        orders: list[Order] | None,
        page_size: int | None,
        page_number: int | None,
    ):
        if filters is not None:
            if not all(isinstance(filter, Filter) for filter in filters):
                raise TypeError("Filters must be a list of Filter")
        if orders is not None:
            if not all(isinstance(order, Order) for order in orders):
                raise TypeError("Orders must be a list of Order")
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
    def filters(self) -> list[Filter] | None:
        return self._filters

    @property
    def orders(self) -> list[Order] | None:
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
            return len(self._filters) > 0

    @property
    def has_orders(self) -> bool:
        if self._orders is not None:
            return len(self._orders) > 0

    @classmethod
    def from_primitives(
        cls,
        filters: list[dict] | None,
        orders: list[dict] | None,
        page_size: int | None,
        page_number: int | None,
    ) -> "Criteria":
        if filters is not None:
            filters = [Filter.from_primitives(**filter) for filter in filters]
        if orders is not None:
            orders = [Order.from_primitives(**order) for order in orders]
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
