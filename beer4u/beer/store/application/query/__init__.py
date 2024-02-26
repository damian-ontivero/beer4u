from .find_by_id_query import FindStoreByIdQuery
from .find_by_id_query_handler import FindStoreByIdQueryHandler
from .search_all_query import SearchAllStoreQuery
from .search_all_query_handler import SearchAllStoreQueryHandler

STORE_QUERY_HANDLERS = {
    FindStoreByIdQuery: FindStoreByIdQueryHandler,
    SearchAllStoreQuery: SearchAllStoreQueryHandler,
}
