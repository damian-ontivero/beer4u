from beer4u.shared.infrastructure.bus.command.in_memory_command_bus import (
    InMemoryCommandBus,
)

COMMAND_HANDLER_MAPPING = {}


def register_command():
    for command, handler in COMMAND_HANDLER_MAPPING.items():
        InMemoryCommandBus().register(command, handler)
