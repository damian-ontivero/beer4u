from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import Query, QueryHandler

from .find_by_id_query import FindStoreByIdQuery


class FindStoreByIdQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @staticmethod
    def subscribe_to() -> Query:
        return FindStoreByIdQuery

    def handle(self, query: FindStoreByIdQuery) -> Store:
        store = self._repository.search(query.id)
        if store is None:
            raise Exception(f"Store with id {query.id} not found")
        return store
