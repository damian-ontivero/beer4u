from beer4u.shared.domain.bus.command.command import Command
from beer4u.shared.domain.bus.command.command_bus import CommandBus
from beer4u.shared.domain.bus.command.command_handler import CommandHandler


class InMemoryCommandBus(CommandBus):
    _instance = None

    def __new__(cls) -> "InMemoryCommandBus":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._handlers = {}
        return cls._instance

    def register(self, command: Command, handler: CommandHandler) -> None:
        if not issubclass(command, Command):
            raise TypeError(
                "Invalid command type: {c}. Expected: Command".format(
                    c=command.__class__.__name__
                )
            )
        if not isinstance(handler, CommandHandler):
            raise TypeError(
                "Invalid handler type: {c}. Expected: CommandHandler".format(
                    c=handler.__class__.__name__
                )
            )
        if type(command) in self._handlers:
            raise NotImplementedError(
                f"Command {type(command)} is already registered"
            )
        self._handlers[command] = handler

    def dispatch(self, command: Command) -> None:
        if not isinstance(command, Command):
            raise TypeError(
                "Invalid command type: {c}. Expected: Command".format(
                    c=command.__class__.__name__
                )
            )
        if type(command) not in self._handlers:
            raise NotImplementedError(
                "No registered handler found for command: {c}".format(
                    c=command.__class__.__name__
                )
            )
        handler = self._handlers[type(command)]
        handler.handle(command)
