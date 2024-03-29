from abc import ABCMeta, abstractmethod

from .command import Command


class CommandBus(metaclass=ABCMeta):

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class RegisteredCommandError(Exception):

    def __init__(self, command: Command) -> None:
        self._command = command

    def __str__(self) -> str:
        return f"Command: {self._command.__class__.__name__!r} not registered"
