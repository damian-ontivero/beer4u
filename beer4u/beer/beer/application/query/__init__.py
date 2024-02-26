from .find_by_id_query import FindBeerByIdQuery
from .find_by_id_query_handler import FindBeerByIdQueryHandler
from .search_all_query import SearchAllBeerQuery
from .search_all_query_handler import SearchAllBeerQueryHandler

BEER_QUERY_HANDLERS = {
    FindBeerByIdQuery: FindBeerByIdQueryHandler,
    SearchAllBeerQuery: SearchAllBeerQueryHandler,
}
