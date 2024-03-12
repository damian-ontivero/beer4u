from abc import ABCMeta, abstractmethod
from pathlib import Path

from .container import Container
from .service import Service


class Loader(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, container: Container) -> None:
        self._container = container
        self._file_path = None

    @abstractmethod
    def load(self, file_path: str) -> None:
        raise NotImplementedError

    @property
    def container(self) -> Container:
        return self._container

    @property
    def file_path(self) -> Path | None:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str):
        self._file_path = Path(__file__).parent.joinpath(file_path)

    def _parse_imports(self, imports: list[dict]) -> None:
        for import_ in imports:
            self.load(import_["resource"])

    def _parse_services(self, services: dict) -> None:
        for service_id, service in services.items():
            self._parse_service(service_id, service)

    def _parse_service(self, service_id: str, service: dict) -> None:
        self._container.register_service(
            service_id,
            Service(
                service.get("class", None),
                service.get("factory_method", None),
                service.get("arguments", []),
                service.get("tags", []),
            ),
        )
