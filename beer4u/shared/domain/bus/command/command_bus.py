from abc import ABCMeta, abstractmethod

from .command import Command


class CommandBus(metaclass=ABCMeta):

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class CommandNotRegisteredError(Exception):

    def __init__(self, command: Command):
        super().__init__(f"No handler for {command.__name__}")
