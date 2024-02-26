from beer4u.shared.domain.bus.command import (
    Command,
    CommandBus,
    CommandHandler,
    CommandNotRegisteredError,
)


class InMemoryCommandBus(CommandBus):

    def __init__(
        self, command_handler_map: dict[Command, CommandHandler]
    ) -> None:
        self._command_handler_map = command_handler_map

    def dispatch(self, command: Command) -> None:
        handler = self._command_handler_map.get(type(command))
        if handler is None:
            raise CommandNotRegisteredError(command)
        handler.handle(command)
