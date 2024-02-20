from beer4u.beer.beer.domain import BeerRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .delete_command import DeleteBeerCommand


class DeleteBeerCommandHandler(CommandHandler):
    def __init__(self, repository: BeerRepository):
        self.repository = repository

    def handle(self, command: DeleteBeerCommand):
        beer = self.repository.search(command.id)
        if beer is None:
            raise Exception(f"Beer with id {command.id} not found")
        self.repository.delete(beer.id.value)
