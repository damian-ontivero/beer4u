from .container import Container
from .yaml_loader import YAMLLoader

container_ = Container()
loader = YAMLLoader(container_)
loader.load("./resources.yaml")
