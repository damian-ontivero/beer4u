from src.contexts.beer.beer.domain import Beer, BeerRepository
from src.contexts.shared.domain.bus.query import QueryHandler
from src.contexts.shared.domain.exception import NotFound

from .find_by_id_query import FindBeerByIdQuery


class FindBeerByIdQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    def handle(self, query: FindBeerByIdQuery) -> Beer:
        beer = self._repository.search(query.id)
        if beer is None:
            raise NotFound(f"Beer with id {query.id} not found")
        return beer
