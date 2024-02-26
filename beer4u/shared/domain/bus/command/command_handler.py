from abc import ABCMeta, abstractmethod

from .command import Command


class CommandHandler(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, command: Command) -> None:
        raise NotImplementedError
