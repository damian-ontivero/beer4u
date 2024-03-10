class DIContainer:

    def __init__(self):
        self._dependencies = {}

    def register(self, dependency, implementation):
        self._dependencies[dependency] = implementation

    def resolve(self, dependency):
        implementation = self._dependencies.get(dependency)
        if implementation is None:
            raise DependencyNotRegisteredException(dependency)
        return implementation


class DependencyNotRegisteredException(Exception):

    def __init__(self, dependency):
        self._dependency = dependency

    def __str__(self):
        return f"Dependency {self._dependency} is not registered"
