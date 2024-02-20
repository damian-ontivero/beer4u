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
from beer4u.shared.infrastructure.persistence.sqlite.db import SqliteSession

COMMAND_HANDLER_MAPPING = {
    RegisterStoreCommand: RegisterStoreCommandHandler(
        repository=SqliteStoreRepository(SqliteSession)
    ),
    UpdateStoreCommand: UpdateStoreCommandHandler(
        repository=SqliteStoreRepository(SqliteSession)
    ),
    DeleteStoreCommand: DeleteStoreCommandHandler(
        repository=SqliteStoreRepository(SqliteSession)
    ),
}


def register_command_handlers():
    for command, handler in COMMAND_HANDLER_MAPPING.items():
        InMemoryCommandBus().register(command, handler)
