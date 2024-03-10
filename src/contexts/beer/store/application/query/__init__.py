from .find_by_id_query import FindStoreByIdQuery
from .find_by_id_query_handler import FindStoreByIdQueryHandler
from .search_all_query import SearchAllStoreQuery
from .search_all_query_handler import SearchAllStoreQueryHandler
from .search_by_criteria_query import SearchStoreByCriteriaQuery
from .search_by_criteria_query_handler import SearchStoreByCriteriaQueryHandler

STORE_QUERY_HANDLERS = {
    SearchStoreByCriteriaQuery: SearchStoreByCriteriaQueryHandler,
    FindStoreByIdQuery: FindStoreByIdQueryHandler,
    SearchAllStoreQuery: SearchAllStoreQueryHandler,
}
