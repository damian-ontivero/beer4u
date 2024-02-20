from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import QueryHandler

from .search_all_query import SearchAllStoreQuery


class SearchAllStoreQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    def handle(self, query: SearchAllStoreQuery) -> list[Store]:
        return self._repository.search_all()
