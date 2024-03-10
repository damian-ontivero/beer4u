from beer4u.beer.store.application.command import (
    RegisterStoreCommand,
    RegisterStoreCommandHandler,
)
from tests.utils.factories.store_factory import StoreFactory


def test_register__ok(mock_store_repository):
    store = StoreFactory()
    data = store.to_primitives()

    command = RegisterStoreCommand(
        data["name"], data["address"], data["phone"], data["discarded"]
    )
    handler = RegisterStoreCommandHandler(mock_store_repository)

    handler.handle(command)
