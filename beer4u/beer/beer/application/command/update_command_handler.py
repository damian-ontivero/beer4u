from beer4u.beer.beer.domain import BeerRepository
from beer4u.shared.domain.bus.command import Command, CommandHandler

from .update_command import UpdateBeerCommand


class UpdateBeerCommandHandler(CommandHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    @property
    def subscribe_to(self) -> Command:
        return UpdateBeerCommand

    def handle(self, command: UpdateBeerCommand) -> None:
        beer = self._repository.search(command.id)
        if beer is None:
            raise Exception(f"Beer with id {command.id} not found")
        beer.update(
            name=command.name,
            type=command.type,
            alcohol=command.alcohol,
            description=command.description,
        )
        self._repository.save(beer)
