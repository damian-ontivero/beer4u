import importlib

from .service import Service


class InstanceManager:

    def __init__(self, services: dict[Service]) -> None:
        self._services = services

    def get_instance(self, id: str) -> object:
        service = self._services.get(id)
        if service is None:
            raise ValueError(f"Service: {id!r} not found")
        return self._create_instance(service)

    def _create_instance(self, service: Service) -> object:
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

    def _resolve_arguments(self, arguments: list) -> list:
        resolved_arguments = []
        for argument in arguments:
            if isinstance(argument, str) and argument.startswith("@"):
                resolved_arguments.append(self.get_instance(argument[1:]))
            elif isinstance(argument, str) and argument.startswith("!tagged"):
                tag = argument.split(" ")[1]
                resolved_arguments.append(
                    [
                        self.get_instance(name)
                        for name, service in self._services.items()
                        if tag in service.tags
                    ]
                )
            else:
                resolved_arguments.append(argument)
        return resolved_arguments
