from dataclasses import dataclass

from beer4u.shared.domain.bus.command import Command


@dataclass(frozen=True)
class DeleteBeerCommand(Command):
    id: str
