import importlib
import os

import yaml

from .resource import Resource


class Container:

    def __init__(self, path: str):
        self._path = os.path.join(os.path.dirname(__file__), path)
        self._services = {}

    def load(self):
        yaml.add_constructor(
            "!tagged",
            lambda loader, node: "!tagged " + loader.construct_scalar(node),
        )
        with open(self._path, "r") as file:
            data: dict = yaml.load(file, Loader=yaml.FullLoader)
            resources: list = data.get("resources")
            for resource in resources:
                resource_path = os.path.join(
                    os.path.dirname(self._path), resource
                )
                resource = Resource(resource_path)
                self._services.update(resource.get_services())

    def get(self, name: str):
        service = self._services.get(name)
        if service is None:
            raise ValueError(f"Service {name!r} not found")
        return self._create_instance(service)

    def _create_instance(self, service):
        module_name, class_name = service.class_.rsplit(".", 1)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        if service.factory_method:
            if service.arguments:
                arguments = self._resolve_arguments(service.arguments)
                return getattr(class_, service.factory_method)(*arguments)
            return getattr(class_, service.factory_method)()
        if service.arguments:
            arguments = self._resolve_arguments(service.arguments)
            return class_(*arguments)
        return class_()

    def _resolve_arguments(self, arguments):
        resolved_arguments = []
        for argument in arguments:
            if isinstance(argument, str) and argument.startswith("@"):
                resolved_arguments.append(self.get(argument[1:]))
            elif isinstance(argument, str) and argument.startswith("!tagged"):
                tag = argument.split(" ")[1]
                resolved_arguments.append(
                    [
                        self.get(name)
                        for name, service in self._services.items()
                        if tag in service.tags
                    ]
                )
            else:
                resolved_arguments.append(argument)
        return resolved_arguments


container = Container("resources.yaml")
container.load()
