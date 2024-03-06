from dataclasses import dataclass


@dataclass
class SearchStoreByCriteriaQuery:
    filter: dict | None
    sort: list | None
    page_size: int | None
    page_number: int | None
