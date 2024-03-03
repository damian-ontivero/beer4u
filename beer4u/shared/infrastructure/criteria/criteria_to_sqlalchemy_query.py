from sqlalchemy.orm import Query

from beer4u.shared.domain.criteria import Criteria
from beer4u.shared.infrastructure.persistence.sqlite.db import Base


def equals_filter(m, k, v):
    return getattr(m, k).is_(v)


def not_equals_filter(m, k, v):
    return getattr(m, k).isnot(v)


def contains_filter(m, k, v):
    return getattr(m, k).ilike(f"%{v}%")


def not_contains_filter(m, k, v):
    return getattr(m, k).notilike(f"%{v}%")


def is_any_of_filter(m, k, v):
    return getattr(m, k).in_(v.split(","))


def is_not_any_of_filter(m, k, v):
    return getattr(m, k).notin_(v.split(","))


def is_empty_filter(m, k, v):
    return getattr(m, k).is_(None)


def is_not_empty_filter(m, k, v):
    return getattr(m, k).isnot(None)


def starts_with_filter(m, k, v):
    return getattr(m, k).istartswith(f"{v}%")


def ends_with_filter(m, k, v):
    return getattr(m, k).iendswith(f"%{v}")


def gt_filter(m, k, v):
    return getattr(m, k) > v


def ge_filter(m, k, v):
    return getattr(m, k) >= v


def lt_filter(m, k, v):
    return getattr(m, k) < v


def le_filter(m, k, v):
    return getattr(m, k) <= v


FILTER_OPERATOR_MAPPER = {
    "EQUALS": equals_filter,
    "NOT_EQUALS": not_equals_filter,
    "CONTAINS": contains_filter,
    "NOT_CONTAINS": not_contains_filter,
    "IS_ANY_OF": is_any_of_filter,
    "IS_NOT_ANY_OF": is_not_any_of_filter,
    "IS_EMPTY": is_empty_filter,
    "IS_NOT_EMPTY": is_not_empty_filter,
    "STARTS_WITH": starts_with_filter,
    "ENDS_WITH": ends_with_filter,
    "GT": gt_filter,
    "GE": ge_filter,
    "LT": lt_filter,
    "LE": le_filter,
}


def criteria_to_sqlalchemy_query(
    query: Query, model: Base, criteria: Criteria
):
    if criteria.has_filters:
        for filter in criteria.filters:
            filter_operator = FILTER_OPERATOR_MAPPER[filter.operator]
            query = query.filter(
                filter_operator(model, filter.field, filter.value)
            )

    if criteria.has_orders:
        for order in criteria.orders:
            query = query.order_by(
                getattr(model, order.order_by).asc()
                if order.order_type == "ASC"
                else getattr(model, order.order_by).desc()
            )
    return query
