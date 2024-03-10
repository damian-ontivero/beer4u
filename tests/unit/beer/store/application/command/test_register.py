from src.contexts.beer.store.application.command import (
    RegisterStoreCommand,
    RegisterStoreCommandHandler,
)
from tests.utils.factories.store import StoreFactory


def test_register__ok(mock_store_repository):
    store = StoreFactory()
    data = store.to_primitives()

    command = RegisterStoreCommand(
        data["name"], data["address"], data["phone"], data["discarded"]
    )
    handler = RegisterStoreCommandHandler(mock_store_repository)

    handler.handle(command)
