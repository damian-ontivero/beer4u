import inspect


class IoCContainer:
    def __init__(self):
        self._dependencies = {}

    def register(self, dependency, implementation):
        self._dependencies[dependency] = implementation

    def resolve(self, dependency):

        if isinstance(self._dependencies[dependency], list):
            for dep in self._dependencies[dependency]:
                import ipdb

                ipdb.set_trace()
                signature = inspect.signature(dep)
                parameters = signature.parameters
                dependencies = {
                    param_name: self.resolve(param_val.annotation.__name__)
                    for param_name, param_val in parameters.items()
                }
                return self._dependencies[dependency](**dependencies)
        signature = inspect.signature(self._dependencies[dependency])
        parameters = signature.parameters
        dependencies = {name: self.resolve(name) for name in parameters}
        return self._dependencies[dependency](**dependencies)


class DependencyNotRegisteredError(Exception):
    def __init__(self, dependency):
        super().__init__(f"{dependency} not registered")
