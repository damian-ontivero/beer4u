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

    def __init__(self, dependency: str) -> None:
        self._dependency = dependency

    def __str__(self) -> str:
        return f"Dependency {self._dependency} is not registered"
