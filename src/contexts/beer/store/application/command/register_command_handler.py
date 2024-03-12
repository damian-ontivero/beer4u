from src.contexts.beer.store.domain import Store, StoreRepository
from src.contexts.shared.domain.bus.command import Command, CommandHandler

from .register_command import RegisterStoreCommand


class RegisterStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    @property
    def subscribed_to(self) -> Command:
        return RegisterStoreCommand

    def handle(self, command: RegisterStoreCommand) -> None:
        store = Store.create(command.name, command.address, command.phone)
        self._repository.save(store)
