from beer4u.beer.beer.application.command.delete_command import (
    DeleteBeerCommand,
)
from beer4u.beer.beer.application.command.delete_command_handler import (
    DeleteBeerCommandHandler,
)
from beer4u.beer.beer.application.command.register_command import (
    RegisterBeerCommand,
)
from beer4u.beer.beer.application.command.register_command_handler import (
    RegisterBeerCommandHandler,
)
from beer4u.beer.beer.application.command.update_command import (
    UpdateBeerCommand,
)
from beer4u.beer.beer.application.command.update_command_handler import (
    UpdateBeerCommandHandler,
)
from beer4u.beer.beer.infrastructure.persistence.sqlite.beer_repository import (
    SqliteBeerRepository,
)
from beer4u.shared.infrastructure.bus.command.in_memory_command_bus import (
    InMemoryCommandBus,
)
from beer4u.shared.infrastructure.persistence.sqlite.db import SessionLocal

COMMAND_HANDLER_MAPPING = {
    RegisterBeerCommand: RegisterBeerCommandHandler(
        SqliteBeerRepository(SessionLocal)
    ),
    UpdateBeerCommand: UpdateBeerCommandHandler(
        SqliteBeerRepository(SessionLocal)
    ),
    DeleteBeerCommand: DeleteBeerCommandHandler(
        SqliteBeerRepository(SessionLocal)
    ),
}


def register_command_handlers():
    for command, handler in COMMAND_HANDLER_MAPPING.items():
        InMemoryCommandBus().register(command, handler)
