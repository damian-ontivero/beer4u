from src.contexts.beer.store.domain import Store, StoreRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.criteria import Criteria

from .search_by_criteria_query import SearchStoreByCriteriaQuery


class SearchStoreByCriteriaQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Query:
        return SearchStoreByCriteriaQuery

    def handle(self, query: SearchStoreByCriteriaQuery) -> list[Store]:
        criteria = Criteria.from_primitives(
            query.filter, query.sort, query.page_size, query.page_number
        )
        return self._repository.search_by_criteria(criteria)
