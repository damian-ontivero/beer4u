from src.contexts.beer.store.domain import Store, StoreRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.exception import NotFound

from .find_by_id_query import FindStoreByIdQuery


class FindStoreByIdQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Query:
        return FindStoreByIdQuery

    def handle(self, query: FindStoreByIdQuery) -> Store:
        store = self._repository.search(query.id)
        if store is None:
            raise NotFound(f"Store: {query.id!r} not found")
        return store
