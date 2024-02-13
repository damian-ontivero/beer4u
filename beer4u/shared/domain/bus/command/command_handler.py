from abc import ABCMeta, abstractmethod

from beer4u.shared.domain.bus.command.command import Command


class CommandHandler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, command: Command) -> None:
        raise NotImplementedError
