from abc import ABCMeta, abstractmethod

from .command import Command


class CommandBus(metaclass=ABCMeta):

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class RegisteredCommandError(Exception):
    pass
