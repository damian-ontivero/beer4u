from src.contexts.beer.beer.domain import Beer, BeerRepository
from src.contexts.shared.domain.bus.query import Query, QueryHandler
from src.contexts.shared.domain.criteria import Criteria

from .search_by_criteria_query import SearchBeerByCriteriaQuery


class SearchBeerByCriteriaQueryHandler(QueryHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Query:
        return SearchBeerByCriteriaQuery

    def handle(self, query: SearchBeerByCriteriaQuery) -> list[Beer]:
        criteria = Criteria.from_primitives(
            query.filter, query.sort, query.page_size, query.page_number
        )
        return self._repository.search_by_criteria(criteria)
