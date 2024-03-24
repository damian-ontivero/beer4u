class Address:

    __slots__ = (
        "_street",
        "_city",
        "_state",
        "_zip_code",
    )

    def __new__(
        cls, street: str, city: str, state: str, zip_code: str
    ) -> "Address":
        if not isinstance(street, str):
            raise TypeError("Street must be a string")
        if not len(street) > 0:
            raise ValueError("Street cannot be empty")
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        if not len(city) > 0:
            raise ValueError("City cannot be empty")
        if not isinstance(state, str):
            raise TypeError("State must be a string")
        if not len(state) > 0:
            raise ValueError("State cannot be empty")
        if not isinstance(zip_code, str):
            raise TypeError("Zip code must be a string")
        if not len(zip_code) > 0:
            raise ValueError("Zip code cannot be empty")
        instance = super().__new__(cls)
        instance._street = street
        instance._city = city
        instance._state = state
        instance._zip_code = zip_code
        return instance

    @property
    def street(self) -> str:
        return self._street

    @property
    def city(self) -> str:
        return self._city

    @property
    def state(self) -> str:
        return self._state

    @property
    def zip_code(self) -> str:
        return self._zip_code

    def to_primitives(self) -> dict:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return NotImplemented
        return (
            self._street == other._street
            and self._city == other._city
            and self._state == other._state
            and self._zip_code == other._zip_code
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._street, self._city, self._state, self._zip_code))

    def __repr__(self) -> str:
        return (
            "{c}(street={street!r}, city={city!r}, "
            "state={state!r}, zip_code={zip_code!r})"
        ).format(
            c=self.__class__.__name__,
            street=self._street,
            city=self._city,
            state=self._state,
            zip_code=self._zip_code,
        )
