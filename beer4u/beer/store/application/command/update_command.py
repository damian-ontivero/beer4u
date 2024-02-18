from dataclasses import dataclass

from beer4u.shared.domain.bus.command.command import Command


@dataclass(frozen=True)
class UpdateStoreCommand(Command):
    id: str
    name: str
    address: dict
    phone: str
    discarded: bool
