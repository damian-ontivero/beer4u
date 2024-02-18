from beer4u.beer.beer.application.command.delete_command import (
    DeleteBeerCommand,
)
from beer4u.beer.beer.domain.beer_repository import BeerRepository
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class DeleteBeerCommandHandler(CommandHandler):
    def __init__(self, repository: BeerRepository):
        self.repository = repository

    def handle(self, command: DeleteBeerCommand):
        beer = self.repository.search(command.id)
        if beer is None:
            raise Exception(f"Beer with id {command.id} not found")
        self.repository.delete(beer.id.value)
