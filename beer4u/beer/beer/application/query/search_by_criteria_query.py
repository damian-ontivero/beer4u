from dataclasses import dataclass


@dataclass
class SearchBeerByCriteriaQuery:
    filters: list[dict] | None
    orders: list[dict] | None
    page_size: int | None
    page_number: int | None
