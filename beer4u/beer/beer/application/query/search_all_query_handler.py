from beer4u.beer.beer.application.query.search_all_query import (
    SearchAllBeerQuery,
)
from beer4u.beer.beer.domain.beer import Beer
from beer4u.beer.beer.domain.beer_repository import BeerRepository
from beer4u.shared.domain.bus.query.query_handler import QueryHandler


class SearchAllBeerQueryHandler(QueryHandler):
    def __init__(self, repository: BeerRepository):
        self._repository = repository

    def handle(self, query: SearchAllBeerQuery) -> list[Beer]:
        return self._repository.search_all()
