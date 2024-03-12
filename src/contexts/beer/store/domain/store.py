from src.contexts.shared.domain import Address, AggregateRoot, EntityId


class Store(AggregateRoot):

    def __init__(
        self,
        id: EntityId,
        name: str,
        address: Address,
        phone: str,
        discarded: bool,
    ) -> None:
        super().__init__(id=id, discarded=discarded)
        self._name = name
        self._address = address
        self._phone = phone

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> Address:
        return self._address

    @property
    def phone(self) -> str:
        return self._phone

    @classmethod
    def create(
        cls,
        name: str,
        address: dict,
        phone: str,
    ) -> "Store":
        return cls(
            EntityId.generate(),
            name,
            Address.from_primitives(
                address.get("street"),
                address.get("city"),
                address.get("state"),
                address.get("zip_code"),
            ),
            phone,
            False,
        )

    @classmethod
    def from_primitives(
        cls,
        id: str,
        name: str,
        address: dict,
        phone: str,
        discarded: bool,
    ) -> "Store":
        return cls(
            EntityId.from_text(id),
            name,
            Address.from_primitives(
                address.get("street"),
                address.get("city"),
                address.get("state"),
                address.get("zip_code"),
            ),
            phone,
            discarded,
        )

    def to_primitives(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name,
            "address": self.address.to_primitives(),
            "phone": self.phone,
            "discarded": self.discarded,
        }

    def update(
        self,
        name: str | None = None,
        address: dict | None = None,
        phone: str | None = None,
        discarded: bool | None = None,
    ) -> None:
        if name is not None:
            if not self._name == name:
                self._name = name
        if address is not None:
            if not self._address == address:
                self._address = Address.from_primitives(
                    address.get("street"),
                    address.get("city"),
                    address.get("state"),
                    address.get("zip_code"),
                )
        if phone is not None:
            if not self._phone == phone:
                self._phone = phone
        if discarded is not None:
            if not self.discarded == discarded:
                self.discarded = discarded
