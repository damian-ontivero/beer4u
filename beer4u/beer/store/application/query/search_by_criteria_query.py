from dataclasses import dataclass


@dataclass
class SearchStoreByCriteriaQuery:
    filters: dict | None
    orders: list | None
    page_size: int | None
    page_number: int | None
