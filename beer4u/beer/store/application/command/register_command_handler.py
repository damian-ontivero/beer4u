from beer4u.beer.store.application.command.register_command import (
    RegisterStoreCommand,
)
from beer4u.beer.store.domain.store import Store
from beer4u.beer.store.domain.store_repository import StoreRepository
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class RegisterStoreCommandHandler(CommandHandler):
    def __init__(self, repository: StoreRepository):
        self.repository = repository

    def handle(self, command: RegisterStoreCommand):
        store = Store.create(command.name, command.address, command.phone)
        self.repository.save(store)
