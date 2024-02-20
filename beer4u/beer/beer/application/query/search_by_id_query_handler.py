from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.query import QueryHandler

from .search_by_id_query import SearchBeerByIdQuery


class SearchBeerByIdQueryHandler(QueryHandler):
    def __init__(self, repository: BeerRepository):
        self._repository = repository

    def handle(self, query: SearchBeerByIdQuery) -> Beer:
        beer = self._repository.search(query.id)
        if beer is None:
            raise Exception(f"Beer with id {query.id} not found")
        return beer
