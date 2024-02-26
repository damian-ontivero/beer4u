class IoCContainer:

    def __init__(self):
        self._dependencies = {}

    def register(self, dependency, implementation):
        self._dependencies[dependency] = implementation

    def resolve(self, dependency):
        implementation = self._dependencies.get(dependency)
        if implementation is None:
            raise Exception(f"Dependency {dependency} not found")
        return implementation
