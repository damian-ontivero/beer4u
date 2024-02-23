from beer4u.beer.beer.domain import BeerRepository
from beer4u.shared.domain.bus.command import Command, CommandHandler
from beer4u.shared.domain.bus.query import QueryBus

from .delete_command import DeleteBeerCommand


class DeleteBeerCommandHandler(CommandHandler):

    def __init__(
        self, repository: BeerRepository, query_bus: QueryBus
    ) -> None:
        self._repository = repository
        self._query_bus = query_bus

    @staticmethod
    def subscribe_to() -> Command:
        return DeleteBeerCommand

    def handle(self, command: DeleteBeerCommand) -> None:
        beer = self._repository.search(command.id)
        if beer is None:
            raise Exception(f"Beer with id {command.id} not found")
        store = self._query_bus.ask(command.beer_store_id)
        if store is None:
            raise Exception(f"Store with id {command.beer_store_id} not found")
        beer.discard()
        self._repository.save(beer)
