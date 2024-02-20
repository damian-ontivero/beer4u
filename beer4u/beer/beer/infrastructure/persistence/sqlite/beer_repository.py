from sqlalchemy.orm import Session

from beer4u.beer.beer.domain import Beer, BeerRepository

from .beer import BeerSqliteModel


class SqliteBeerRepository(BeerRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    def search_by_criteria(self) -> list[Beer]:
        with self._session() as session:
            pass

    def search_all(self) -> list[Beer]:
        with self._session() as session:
            beers_db = session.query(BeerSqliteModel).all()
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
            beer_db = session.query(BeerSqliteModel).get(id)
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
            beer_db = session.query(BeerSqliteModel).get(beer.id.value)
            if beer_db:
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
            beer_db = session.query(BeerSqliteModel).get(id)
            session.delete(beer_db)
            session.commit()
