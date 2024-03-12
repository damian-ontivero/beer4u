class Service:

    def __init__(
        self, class_: str, factory_method: str, arguments: list, tags: list
    ):
        self._class_ = class_
        self._factory_method = factory_method
        self._arguments = arguments
        self._tags = tags

    @property
    def class_(self) -> str:
        return self._class_

    @property
    def factory_method(self) -> str:
        return self._factory_method

    @property
    def arguments(self) -> list:
        return self._arguments

    @property
    def tags(self) -> list:
        return self._tags

    def __repr__(self) -> str:
        return (
            "{c}(class_={class_!r}, factory_method={factory_method!r}, "
            "arguments={arguments!r}, tags={tags!r})"
        ).format(
            c=self.__class__.__name__,
            class_=self._class_,
            factory_method=self._factory_method,
            arguments=self._arguments,
            tags=self._tags,
        )
