from sqlalchemy.orm import Session

from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.criteria import Criteria
from beer4u.shared.infrastructure.criteria import criteria_to_sqlalchemy_query

from .store import StoreSqliteModel


class SqliteStoreRepository(StoreRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def search_by_criteria(self, criteria: Criteria) -> list[Store]:
        with self._session() as session:
            query = session.query(StoreSqliteModel)
            query = criteria_to_sqlalchemy_query(
                query, StoreSqliteModel, criteria
            )
            stores_db = query.all()
            return [
                Store.from_primitives(
                    store_db.id,
                    store_db.name,
                    store_db.address,
                    store_db.phone,
                    store_db.discarded,
                )
                for store_db in stores_db
            ]

    def search_all(self) -> list[Store]:
        with self._session() as session:
            stores_db = session.query(StoreSqliteModel).all()
            return [
                Store.from_primitives(
                    store_db.id,
                    store_db.name,
                    store_db.address,
                    store_db.phone,
                    store_db.discarded,
                )
                for store_db in stores_db
            ]

    def search(self, id: str) -> Store | None:
        with self._session() as session:
            store_db = session.query(StoreSqliteModel).get(id)
            if store_db is not None:
                return Store.from_primitives(
                    store_db.id,
                    store_db.name,
                    store_db.address,
                    store_db.phone,
                    store_db.discarded,
                )

    def count(self) -> int:
        with self._session() as session:
            return session.query(StoreSqliteModel).count()

    def save(self, store: Store) -> None:
        with self._session() as session:
            store_db = session.query(StoreSqliteModel).get(store.id.value)
            if store_db:
                store_db.name = store.name
                store_db.address = store.address.to_primitives()
                store_db.phone = store.phone
                store_db.discarded = store.discarded
            else:
                store_db = StoreSqliteModel(
                    id=store.id.value,
                    name=store.name,
                    address=store.address.to_primitives(),
                    phone=store.phone,
                    discarded=store.discarded,
                )
                session.add(store_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            store_db = session.query(StoreSqliteModel).get(id)
            session.delete(store_db)
            session.commit()
