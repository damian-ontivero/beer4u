import os

import yaml


class Container:

    def __init__(self):
        self._base_path = os.path.dirname(os.path.abspath(__file__))
        self._dependencies = {}

    def configure(self, filename: str):
        resources = yaml.safe_load(
            open(os.path.join(self._base_path, filename))
        )
        self._configure_resources(resources.get("resources", []))

    def _configure_resources(self, resources: list):
        for resource in resources:
            services = yaml.safe_load(
                open(os.path.join(self._base_path, resource))
            )


container = Container()
container.configure("config.yaml")
