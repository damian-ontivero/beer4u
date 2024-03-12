from src.contexts.beer.beer.domain import BeerRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.exception import NotFound

from .update_command import UpdateBeerCommand


class UpdateBeerCommandHandler(CommandHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Command:
        return UpdateBeerCommand

    def handle(self, command: UpdateBeerCommand) -> None:
        beer = self._repository.search(command.id)
        if beer is None:
            raise NotFound(f"Beer: {command.id!r} not found")
        beer.update(
            name=command.name,
            type=command.type,
            alcohol=command.alcohol,
            description=command.description,
        )
        self._repository.save(beer)
