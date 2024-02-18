from dataclasses import dataclass

from beer4u.shared.domain.bus.query.query import Query


@dataclass(frozen=True)
class SearchStoreByIdQuery(Query):
    id: str