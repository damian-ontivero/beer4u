import os

import yaml

from .service import Service


class Resource:
    def __init__(self, path: str):
        self._path = os.path.join(os.path.dirname(__file__), path)
        self._services = {}

    @property
    def path(self):
        return self._path

    @property
    def services(self):
        return self._services

    def get_services(self):
        with open(self._path, "r") as file:
            data: dict = yaml.load(file, Loader=yaml.FullLoader)
            services: dict = data.get("services")
            for name, impl in services.items():
                self._services[name] = Service(
                    impl.get("class", None),
                    impl.get("factory_method", None),
                    impl.get("arguments", []),
                    impl.get("tags", []),
                )
        return self._services
