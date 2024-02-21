from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import FindBeerByIdQuery


class FindBeerByIdQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribe_to(self) -> Query:
        return FindBeerByIdQuery

    def handle(self, query: FindBeerByIdQuery) -> Beer:
        beer = self._repository.search(query.id)
        if beer is None:
            raise Exception(f"Beer with id {query.id} not found")
        return beer
