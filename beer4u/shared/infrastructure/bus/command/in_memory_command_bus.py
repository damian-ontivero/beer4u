from beer4u.shared.domain.bus.command import (
    Command,
    CommandBus,
    CommandHandler,
)


class InMemoryCommandBus(CommandBus):

    def __init__(self, command_handlers: list[CommandHandler]):
        self._command_handlers = {
            handler.subscribe_to(): handler for handler in command_handlers
        }

    def dispatch(self, command: Command) -> None:
        self._command_handlers.get(type(command)).handle(command)
