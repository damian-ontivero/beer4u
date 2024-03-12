from src.contexts.beer.store.domain import StoreRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler
from src.contexts.shared.domain.exception import NotFound

from .delete_command import DeleteStoreCommand


class DeleteStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Command:
        return DeleteStoreCommand

    def handle(self, command: DeleteStoreCommand) -> None:
        store = self._repository.search(command.id)
        if store is None:
            raise NotFound(f"Store: {command.id!r} not found")
        store.discard()
        self._repository.save(store)
