from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import Query, QueryHandler

from .search_all_query import SearchAllStoreQuery


class SearchAllStoreQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @staticmethod
    def subscribe_to() -> Query:
        return SearchAllStoreQuery

    def handle(self, query: SearchAllStoreQuery) -> list[Store]:
        return self._repository.search_all()
