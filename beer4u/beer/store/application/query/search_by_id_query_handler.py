from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import QueryHandler

from .search_by_id_query import SearchStoreByIdQuery


class SearchStoreByIdQueryHandler(QueryHandler):
    def __init__(self, repository: StoreRepository):
        self._repository = repository

    def handle(self, query: SearchStoreByIdQuery) -> Store:
        store = self._repository.search(query.id)
        if store is None:
            raise Exception(f"Store with id {query.id} not found")
        return store
