from beer4u.shared.domain import AggregateRoot, EntityId


class Beer(AggregateRoot):

    def __init__(
        self,
        id: EntityId,
        name: str,
        type: str,
        alcohol: float,
        description: str,
        discarded: bool = False,
    ) -> None:
        super().__init__(id=id, discarded=discarded)
        self._name = name
        self._type = type
        self._alcohol = alcohol
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type

    @property
    def alcohol(self) -> float:
        return self._alcohol

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def create(
        cls,
        name: str,
        type: str,
        alcohol: float,
        description: str,
    ) -> "Beer":
        return cls(
            EntityId.generate(),
            name,
            type,
            alcohol,
            description,
            False,
        )

    @classmethod
    def from_primitives(
        cls,
        id: str,
        name: str,
        type: str,
        alcohol: float,
        description: str,
        discarded: bool,
    ) -> "Beer":
        return cls(
            EntityId.from_text(id),
            name,
            type,
            alcohol,
            description,
            discarded,
        )

    def to_primitives(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name,
            "type": self.type,
            "alcohol": self.alcohol,
            "description": self.description,
            "discarded": self.discarded,
        }

    def update(
        self,
        name: str | None = None,
        type: str | None = None,
        alcohol: float | None = None,
        description: str | None = None,
    ) -> None:
        if name is not None:
            if not self._name == name:
                self._name = name
        if type is not None:
            if not self._type == type:
                self._type = type
        if alcohol is not None:
            if not self._alcohol == alcohol:
                self._alcohol = alcohol
        if description is not None:
            if not self._description == description:
                self._description = description

    def discard(self) -> None:
        super().discard()
