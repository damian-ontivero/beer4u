from beer4u.beer.beer.domain import BeerRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .update_command import UpdateBeerCommand


class UpdateBeerCommandHandler(CommandHandler):
    def __init__(self, repository: BeerRepository):
        self.repository = repository

    def handle(self, command: UpdateBeerCommand):
        beer = self.repository.search(command.id)
        if beer is None:
            raise Exception(f"Beer with id {command.id} not found")
        beer.update(
            name=command.name,
            type=command.type,
            alcohol=command.alcohol,
            description=command.description,
        )
        self.repository.save(beer)
