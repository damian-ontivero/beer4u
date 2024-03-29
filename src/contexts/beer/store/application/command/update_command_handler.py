from src.contexts.beer.store.domain import StoreRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.exception import NotFound

from .update_command import UpdateStoreCommand


class UpdateStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Command:
        return UpdateStoreCommand

    def handle(self, command: UpdateStoreCommand) -> None:
        store = self._repository.search(command.id)
        if store is None:
            raise NotFound(f"Store: {command.id!r} not found")
        store.update(
            command.name, command.address, command.phone, command.discarded
        )
        self._repository.save(store)
