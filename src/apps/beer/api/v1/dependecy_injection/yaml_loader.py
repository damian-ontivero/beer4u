import yaml

from .container import Container
from .loader import Loader

yaml.add_constructor(
    "!tagged",
    lambda loader, node: "!tagged " + loader.construct_scalar(node),
)


class YAMLLoader(Loader):

    def __init__(self, container: Container):
        super().__init__(container)

    def load(self, file_path: str) -> None:
        self.file_path = file_path

        try:
            with open(self.file_path, "r") as file:
                data: dict = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.file_path!r} not found")

        self._parse_imports(data.get("imports", []))
        self._parse_services(data.get("services", {}))
