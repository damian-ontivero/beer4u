from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.query import QueryHandler

from .search_all_query import SearchAllBeerQuery


class SearchAllBeerQueryHandler(QueryHandler):
    def __init__(self, repository: BeerRepository):
        self._repository = repository

    def handle(self, query: SearchAllBeerQuery) -> list[Beer]:
        return self._repository.search_all()
