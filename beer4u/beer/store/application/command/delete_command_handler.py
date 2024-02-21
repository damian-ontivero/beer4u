from beer4u.beer.store.domain import StoreRepository
from beer4u.shared.domain.bus.command import Command, CommandHandler

from .delete_command import DeleteStoreCommand


class DeleteStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribe_to(self) -> Command:
        return DeleteStoreCommand

    def handle(self, command: DeleteStoreCommand) -> None:
        store = self._repository.search(command.id)
        if store is None:
            raise Exception(f"Store with id {command.id} not found")
        store.discard()
        self._repository.save(store)
