from beer4u.beer.store.domain import StoreRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .delete_command import DeleteStoreCommand


class DeleteStoreCommandHandler(CommandHandler):
    def __init__(self, repository: StoreRepository):
        self.repository = repository

    def handle(self, command: DeleteStoreCommand):
        store = self.repository.search(command.id)
        if store is None:
            raise Exception(f"Store with id {command.id} not found")
        self.repository.delete(store.id.value)
