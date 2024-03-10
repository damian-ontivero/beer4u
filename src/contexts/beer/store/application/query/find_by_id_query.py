from dataclasses import dataclass

from src.contexts.shared.domain.bus.query import Query


@dataclass(frozen=True)
class FindStoreByIdQuery(Query):
    id: str
