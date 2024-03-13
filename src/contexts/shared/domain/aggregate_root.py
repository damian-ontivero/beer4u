from src.contexts.shared.domain.bus.event.domain_event import DomainEvent
from src.contexts.shared.domain.entity import Entity
from src.contexts.shared.domain.entity_id import EntityId


class AggregateRoot(Entity):
    """
    Base class for aggregate roots.

    Aggregate roots encapsulate a group of entities and value objects.
    They ensure the aggregate is always in a consistent state and contain
    the domain events raised by the aggregate.
    """

    def __init__(self, id: EntityId, discarded: bool = False) -> None:
        super().__init__(id, discarded)
        self._domain_events = []

    @property
    def domain_events(self) -> list[DomainEvent]:
        return self._domain_events

    def _register_domain_event(self, domain_event: DomainEvent) -> None:
        if domain_event is None:
            raise RegisteredDomainEventError("Domain event is None")
        self._domain_events.append(domain_event)

    def clear_domain_events(self) -> None:
        self._domain_events.clear()


class RegisteredDomainEventError(Exception):
    pass
