from beer4u.beer.store.application.query.search_by_id_query import (
    SearchStoreByIdQuery,
)
from beer4u.beer.store.domain.store import Store
from beer4u.beer.store.domain.store_repository import StoreRepository
from beer4u.shared.domain.bus.query.query_handler import QueryHandler


class SearchStoreByIdQueryHandler(QueryHandler):
    def __init__(self, repository: StoreRepository):
        self._repository = repository

    def handle(self, query: SearchStoreByIdQuery) -> Store:
        store = self._repository.search(query.id)
        if store is None:
            raise Exception(f"Store with id {query.id} not found")
        return store
