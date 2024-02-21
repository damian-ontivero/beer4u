from beer4u.beer.beer.domain import Beer, BeerRepository
from beer4u.shared.domain.bus.command import Command, CommandHandler

from .register_command import RegisterBeerCommand


class RegisterBeerCommandHandler(CommandHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribe_to(self) -> Command:
        return RegisterBeerCommand

    def handle(self, command: RegisterBeerCommand) -> None:
        beer = Beer.create(
            command.name, command.type, command.alcohol, command.description
        )
        self._repository.save(beer)
