from beer4u.beer.store.application.command.update_command import (
    UpdateStoreCommand,
)
from beer4u.beer.store.domain.store_repository import StoreRepository
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class UpdateStoreCommandHandler(CommandHandler):
    def __init__(self, repository: StoreRepository):
        self.repository = repository

    def handle(self, command: UpdateStoreCommand):
        store = self.repository.search(command.id)
        if store is None:
            raise Exception(f"Store with id {command.id} not found")
        store.update(
            command.name, command.address, command.phone, command.discarded
        )
        self.repository.save(store)
