from uuid import uuid4


class EntityId:

    __slots__ = ("_value",)

    @classmethod
    def generate(cls) -> "EntityId":
        return cls(uuid4().hex)

    @classmethod
    def from_text(cls, text: str) -> "EntityId":
        return cls(text)

    def __new__(cls, value: str) -> "EntityId":
        if not isinstance(value, str):
            raise TypeError("Entity Id must be a string")
        if not len(value) > 0:
            raise ValueError("Entity Id must not be empty")
        instance = super().__new__(cls)
        instance._value = value
        return instance

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return ("{c}(value={value!r})").format(
            c=self.__class__.__name__, value=self._value
        )
