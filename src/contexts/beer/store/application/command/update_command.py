from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class UpdateStoreCommand(Command):
    id: str
    name: str
    address: dict
    phone: str
    discarded: bool
