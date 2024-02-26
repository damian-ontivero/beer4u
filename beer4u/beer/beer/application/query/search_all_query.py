from dataclasses import dataclass

from beer4u.shared.domain.bus.query import Query


@dataclass(frozen=True)
class SearchAllBeerQuery(Query):
    pass
