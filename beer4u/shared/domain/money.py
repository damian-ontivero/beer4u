class Money:
    __slots__ = ("_currency", "_amount")

    def __new__(cls, currency: str, amount: float) -> "Money":
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string")
        if not len(currency) > 0:
            raise ValueError("Currency cannot be empty")
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        instance = super().__new__(cls)
        instance._currency = currency
        instance._amount = amount
        return instance

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def __dict__(self) -> dict:
        return {"currency": self._currency, "amount": self._amount}

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Money):
            return (
                self._currency == other._currency
                and self._amount == other._amount
            )
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self._currency, self._amount))

    def __repr__(self) -> str:
        return "{c}(currency={currency!r}, amount={amount!r})".format(
            c=self.__class__.__name__,
            currency=self._currency,
            amount=self._amount,
        )
