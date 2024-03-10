from .find_by_id_query import FindBeerByIdQuery
from .find_by_id_query_handler import FindBeerByIdQueryHandler
from .search_all_query import SearchAllBeerQuery
from .search_all_query_handler import SearchAllBeerQueryHandler
from .search_by_criteria_query import SearchBeerByCriteriaQuery
from .search_by_criteria_query_handler import SearchBeerByCriteriaQueryHandler

BEER_QUERY_HANDLERS = {
    SearchBeerByCriteriaQuery: SearchBeerByCriteriaQueryHandler,
    FindBeerByIdQuery: FindBeerByIdQueryHandler,
    SearchAllBeerQuery: SearchAllBeerQueryHandler,
}
