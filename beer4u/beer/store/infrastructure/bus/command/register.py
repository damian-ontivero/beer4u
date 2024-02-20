from beer4u.beer.store.application.command import (
    DeleteStoreCommand,
    DeleteStoreCommandHandler,
    RegisterStoreCommand,
    RegisterStoreCommandHandler,
    UpdateStoreCommand,
    UpdateStoreCommandHandler,
)
from beer4u.beer.store.infrastructure.persistence.sqlite import (
    SqliteStoreRepository,
)
from beer4u.shared.infrastructure.bus.command import InMemoryCommandBus
from beer4u.shared.infrastructure.persistence.sqlite.db import SessionLocal

COMMAND_HANDLER_MAPPING = {
    RegisterStoreCommand: RegisterStoreCommandHandler(
        repository=SqliteStoreRepository(SessionLocal)
    ),
    UpdateStoreCommand: UpdateStoreCommandHandler(
        repository=SqliteStoreRepository(SessionLocal)
    ),
    DeleteStoreCommand: DeleteStoreCommandHandler(
        repository=SqliteStoreRepository(SessionLocal)
    ),
}


def register_command_handlers():
    for command, handler in COMMAND_HANDLER_MAPPING.items():
        InMemoryCommandBus().register(command, handler)
