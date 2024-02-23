from abc import ABCMeta, abstractmethod

from .command import Command


class CommandHandler(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe_to() -> Command:
        raise NotImplementedError

    @abstractmethod
    def handle(self, command: Command) -> None:
        raise NotImplementedError
