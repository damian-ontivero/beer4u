from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.query import QueryHandler
from beer4u.shared.domain.criteria import Criteria

from .search_by_criteria_query import SearchStoreByCriteriaQuery


class SearchStoreByCriteriaQueryHandler(QueryHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    def handle(self, query: SearchStoreByCriteriaQuery) -> list[Store]:
        criteria = Criteria.from_primitives(
            query.filters, query.orders, query.page_size, query.page_number
        )
        return self._repository.search_by_criteria(criteria)
