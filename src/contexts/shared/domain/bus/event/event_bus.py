from abc import ABCMeta, abstractmethod

from src.contexts.shared.domain import DomainEvent


class EventBus(metaclass=ABCMeta):

    @abstractmethod
    def publish(self, domain_event: DomainEvent) -> None:
        raise NotImplementedError
