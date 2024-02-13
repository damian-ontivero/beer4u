from abc import ABCMeta, abstractmethod

from beer4u.shared.domain.domain_event import DomainEvent


class EventBus(metaclass=ABCMeta):
    @abstractmethod
    def publish(self, domain_event: DomainEvent) -> None:
        raise NotImplementedError
