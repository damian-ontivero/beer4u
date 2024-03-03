from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.query import QueryHandler
from beer4u.shared.domain.criteria import Criteria

from .search_by_criteria_query import SearchBeerByCriteriaQuery


class SearchBeerByCriteriaQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    def handle(self, query: SearchBeerByCriteriaQuery) -> list[Beer]:
        criteria = Criteria.from_primitives(
            query.filters, query.orders, query.page_size, query.page_number
        )
        return self._repository.search_by_criteria(criteria)
