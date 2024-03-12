from src.contexts.beer.beer.domain import Beer, BeerRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.exception import NotFound

from .find_by_id_query import FindBeerByIdQuery


class FindBeerByIdQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Query:
        return FindBeerByIdQuery

    def handle(self, query: FindBeerByIdQuery) -> Beer:
        beer = self._repository.search(query.id)
        if beer is None:
            raise NotFound(f"Beer: {query.id!r} not found")
        return beer
