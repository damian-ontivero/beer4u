from sqlalchemy.orm import Session

from src.contexts.beer.beer.domain import Beer, BeerRepository
from src.contexts.shared.domain.criteria import Criteria
from src.contexts.shared.infrastructure.criteria import (
    criteria_to_sqlalchemy_query,
)

from .beer import BeerSqliteModel


class SqliteBeerRepository(BeerRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def search_by_criteria(self, criteria: Criteria) -> list[Beer]:
        with self._session() as session:
            query = session.query(BeerSqliteModel)
            query = criteria_to_sqlalchemy_query(
                query, BeerSqliteModel, criteria
            )
            beers_db = query.all()

            return [
                Beer.from_primitives(
                    beer_db.id,
                    beer_db.name,
                    beer_db.type,
                    beer_db.alcohol,
                    beer_db.description,
                    beer_db.discarded,
                )
                for beer_db in beers_db
            ]

    def search_all(self) -> list[Beer]:
        with self._session() as session:
            query = session.query(BeerSqliteModel)
            beers_db = query.all()

            return [
                Beer.from_primitives(
                    beer_db.id,
                    beer_db.name,
                    beer_db.type,
                    beer_db.alcohol,
                    beer_db.description,
                    beer_db.discarded,
                )
                for beer_db in beers_db
            ]

    def search(self, id: str) -> Beer | None:
        with self._session() as session:
            beer_db = session.get(BeerSqliteModel, id)

            if beer_db is not None:
                return Beer.from_primitives(
                    beer_db.id,
                    beer_db.name,
                    beer_db.type,
                    beer_db.alcohol,
                    beer_db.description,
                    beer_db.discarded,
                )

    def count(self) -> int:
        with self._session() as session:
            return session.query(BeerSqliteModel).count()

    def save(self, beer: Beer) -> None:
        with self._session() as session:
            beer_db = session.get(BeerSqliteModel, beer.id.value)

            if beer_db is not None:
                beer_db.name = beer.name
                beer_db.type = beer.type
                beer_db.alcohol = beer.alcohol
                beer_db.description = beer.description
                beer_db.discarded = beer.discarded
            else:
                beer_db = BeerSqliteModel(
                    id=beer.id.value,
                    name=beer.name,
                    type=beer.type,
                    alcohol=beer.alcohol,
                    description=beer.description,
                    discarded=beer.discarded,
                )
                session.add(beer_db)
            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            beer_db = session.get(BeerSqliteModel, id)
            session.delete(beer_db)
            session.commit()
