from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import QueryHandler
from beer4u.shared.domain.exception import NotFound

from .find_by_id_query import FindStoreByIdQuery


class FindStoreByIdQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    def handle(self, query: FindStoreByIdQuery) -> Store:
        store = self._repository.search(query.id)
        if store is None:
            raise NotFound(f"Store with id {query.id} not found")
        return store
