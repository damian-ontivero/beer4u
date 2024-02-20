from beer4u.beer.store.domain import Store, StoreRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .register_command import RegisterStoreCommand


class RegisterStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    def handle(self, command: RegisterStoreCommand) -> None:
        store = Store.create(command.name, command.address, command.phone)
        self._repository.save(store)
