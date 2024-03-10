from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class RegisterStoreCommand(Command):
    name: str
    address: dict
    phone: str