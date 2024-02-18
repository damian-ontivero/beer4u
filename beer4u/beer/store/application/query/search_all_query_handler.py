from beer4u.beer.store.application.query.search_all_query import (
    SearchAllStoreQuery,
)
from beer4u.beer.store.domain.store import Store
from beer4u.beer.store.domain.store_repository import StoreRepository
from beer4u.shared.domain.bus.query.query_handler import QueryHandler


class SearchAllStoreQueryHandler(QueryHandler):
    def __init__(self, repository: StoreRepository):
        self._repository = repository

    def handle(self, query: SearchAllStoreQuery) -> list[Store]:
        return self._repository.search_all()
