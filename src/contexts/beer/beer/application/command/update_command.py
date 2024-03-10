from dataclasses import dataclass

from src.contexts.shared.domain.bus.command import Command


@dataclass(frozen=True)
class UpdateBeerCommand(Command):
    id: str
    name: str
    type: str
    alcohol: float
    description: str
