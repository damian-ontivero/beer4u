from dataclasses import dataclass

from beer4u.shared.domain.bus.command import Command


@dataclass(frozen=True)
class RegisterStoreCommand(Command):
    name: str
    address: dict
    phone: str
