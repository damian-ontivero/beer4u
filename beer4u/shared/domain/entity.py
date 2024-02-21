from abc import ABCMeta, abstractmethod

from beer4u.shared.domain.domain_event import DomainEvent
from beer4u.shared.domain.entity_id import EntityId


class Entity(metaclass=ABCMeta):
    """
    Abstract base class for entities.

    Entities are domain objects with unique identity and defined by attributes.
    They have a specific life cycle: creation, update, and deletion. They are
    mutable and can be compared by their identity.
    """

    class Created(DomainEvent):
        pass

    class Modified(DomainEvent):
        pass

    class Discarded(DomainEvent):
        pass

    @abstractmethod
    def __init__(self, id: EntityId, discarded: bool = False) -> None:
        if id is None:
            raise ValueError("Entity Id must not be None")
        self._id = id
        self._discarded = discarded

    @property
    def id(self) -> EntityId:
        self._check_not_discarded()
        return self._id

    @property
    def discarded(self) -> bool:
        return self._discarded

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self._id == other._id
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self._id)

    def _check_not_discarded(self) -> None:
        if self.discarded:
            raise DiscardedEntityError("The entity is discarded")

    def discard(self) -> None:
        self._check_not_discarded()
        self._discarded = True


class DiscardedEntityError(Exception):
    """Raised when an operation is attempted on a discarded entity."""

    pass
