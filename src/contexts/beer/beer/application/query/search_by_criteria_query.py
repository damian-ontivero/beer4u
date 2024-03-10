from dataclasses import dataclass


@dataclass
class SearchBeerByCriteriaQuery:
    filter: dict | None
    sort: list | None
    page_size: int | None
    page_number: int | None
