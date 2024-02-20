from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .register_command import RegisterBeerCommand


class RegisterBeerCommandHandler(CommandHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    def handle(self, command: RegisterBeerCommand) -> None:
        beer = Beer.create(
            command.name, command.type, command.alcohol, command.description
        )
        self._repository.save(beer)
