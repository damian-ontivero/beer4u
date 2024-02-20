from beer4u.beer.store.application.command.delete_command import (
    DeleteStoreCommand,
)
from beer4u.beer.store.application.command.delete_command_handler import (
    DeleteStoreCommandHandler,
)
from beer4u.beer.store.application.command.register_command import (
    RegisterStoreCommand,
)
from beer4u.beer.store.application.command.register_command_handler import (
    RegisterStoreCommandHandler,
)
from beer4u.beer.store.application.command.update_command import (
    UpdateStoreCommand,
)
from beer4u.beer.store.application.command.update_command_handler import (
    UpdateStoreCommandHandler,
)
from beer4u.beer.store.infrastructure.persistence.sqlite.store_repository import (
    SqliteStoreRepository,
)
from beer4u.shared.infrastructure.bus.command.in_memory_command_bus import (
    InMemoryCommandBus,
)
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
