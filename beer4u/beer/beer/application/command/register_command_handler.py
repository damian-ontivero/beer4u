from beer4u.beer.beer.application.command.register_command import (
    RegisterBeerCommand,
)
from beer4u.beer.beer.domain.beer import Beer
from beer4u.beer.beer.domain.beer_repository import BeerRepository
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class RegisterBeerCommandHandler(CommandHandler):
    def __init__(self, repository: BeerRepository):
        self.repository = repository

    def handle(self, command: RegisterBeerCommand):
        beer = Beer.create(
            command.name, command.type, command.alcohol, command.description
        )
        self.repository.save(beer)
