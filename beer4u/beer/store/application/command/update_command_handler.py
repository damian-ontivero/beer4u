from beer4u.beer.store.domain import StoreRepository
from beer4u.shared.domain.bus.command import CommandHandler

from .update_command import UpdateStoreCommand


class UpdateStoreCommandHandler(CommandHandler):

    def __init__(self, repository: StoreRepository) -> None:
        self._repository = repository

    def handle(self, command: UpdateStoreCommand) -> None:
        store = self._repository.search(command.id)
        if store is None:
            raise Exception(f"Store with id {command.id} not found")
        store.update(
            command.name, command.address, command.phone, command.discarded
        )
        self._repository.save(store)
