from src.contexts.beer.beer.domain import Beer, BeerRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler

from .search_all_query import SearchAllBeerQuery


class SearchAllBeerQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Query:
        return SearchAllBeerQuery

    def handle(self, query: SearchAllBeerQuery) -> list[Beer]:
        return self._repository.search_all()
