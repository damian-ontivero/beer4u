from beer4u.beer.beer.application.command import (
    RegisterBeerCommand,
    RegisterBeerCommandHandler,
)
from tests.utils.factories.beer_factory import BeerFactory


def test_register__ok(mock_beer_repository):
    beer = BeerFactory()
    data = beer.to_primitives()

    command = RegisterBeerCommand(
        data["name"],
        data["type"],
        data["alcohol"],
        data["description"],
    )
    handler = RegisterBeerCommandHandler(mock_beer_repository)

    handler.handle(command)
