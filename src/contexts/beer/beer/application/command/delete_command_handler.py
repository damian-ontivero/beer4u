from src.contexts.beer.beer.domain import BeerRepository
from src.contexts.shared.domain.bus.command import CommandHandler
from src.contexts.shared.domain.exception import NotFound

from .delete_command import DeleteBeerCommand


class DeleteBeerCommandHandler(CommandHandler):

    def __init__(self, repository: BeerRepository) -> None:
        self._repository = repository

    def handle(self, command: DeleteBeerCommand) -> None:
        beer = self._repository.search(command.id)
        if beer is None:
            raise NotFound(f"Beer with id {command.id} not found")
        beer.discard()
        self._repository.save(beer)
