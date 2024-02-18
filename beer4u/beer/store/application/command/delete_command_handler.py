from beer4u.beer.store.application.command.delete_command import (
    DeleteStoreCommand,
)
from beer4u.beer.store.domain.store_repository import StoreRepository
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class DeleteStoreCommandHandler(CommandHandler):
    def __init__(self, repository: StoreRepository):
        self.repository = repository

    def handle(self, command: DeleteStoreCommand):
        store = self.repository.search(command.id)
        if store is None:
            raise Exception(f"Store with id {command.id} not found")
        self.repository.delete(store.id.value)
