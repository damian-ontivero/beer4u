from abc import ABCMeta, abstractmethod

from .command import Command


class CommandHandler(metaclass=ABCMeta):

    @property
    @abstractmethod
    def subscribed_to(self) -> Command:
        raise NotImplementedError

    @abstractmethod
    def handle(self, command: Command) -> None:
        raise NotImplementedError
