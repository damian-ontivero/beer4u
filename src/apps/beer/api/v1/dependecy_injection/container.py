from .instance_manager import InstanceManager
from .service import Service


class Container:

    def __init__(self):
        self._services: dict[str, Service] = {}

    @property
    def services(self) -> dict[str, Service]:
        return self._services

    @property
    def instance_manager(self) -> InstanceManager:
        return InstanceManager(self._services)

    def register_service(self, name: str, service: Service):
        self._services[name] = service

    def get(self, service_id: str):
        return self.instance_manager.get_instance(service_id)
