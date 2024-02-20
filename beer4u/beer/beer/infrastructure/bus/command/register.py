from beer4u.beer.beer.application.command import (
    DeleteBeerCommand,
    DeleteBeerCommandHandler,
    RegisterBeerCommand,
    RegisterBeerCommandHandler,
    UpdateBeerCommand,
    UpdateBeerCommandHandler,
)
from beer4u.beer.beer.infrastructure.persistence.sqlite import (
    SqliteBeerRepository,
)
from beer4u.shared.infrastructure.bus.command import InMemoryCommandBus
from beer4u.shared.infrastructure.persistence.sqlite.db import SqliteSession

COMMAND_HANDLER_MAPPING = {
    RegisterBeerCommand: RegisterBeerCommandHandler(
        SqliteBeerRepository(SqliteSession)
    ),
    UpdateBeerCommand: UpdateBeerCommandHandler(
        SqliteBeerRepository(SqliteSession)
    ),
    DeleteBeerCommand: DeleteBeerCommandHandler(
        SqliteBeerRepository(SqliteSession)
    ),
}


def register_command_handlers():
    for command, handler in COMMAND_HANDLER_MAPPING.items():
        InMemoryCommandBus().register(command, handler)
