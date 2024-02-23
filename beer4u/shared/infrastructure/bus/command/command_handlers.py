from beer4u.shared.domain.bus.command import (
    Command,
    CommandHandler,
    CommandNotRegisteredError,
)


class CommandHandlers(dict[Command, CommandHandler]):

    def __init__(self, command_handlers: list[CommandHandler]):
        self._handlers = {
            handler.subscribe_to(): handler for handler in command_handlers
        }

    def get(self, command: Command) -> CommandHandler:
        handler = self._handlers.get(type(command))
        if handler is None:
            raise CommandNotRegisteredError(command)
        return handler
