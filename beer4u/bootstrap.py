import configparser

from beer4u.shared.infrastructure.bus.command import InMemoryCommandBus
from beer4u.shared.infrastructure.bus.event import RabbitMQEventBus
from beer4u.shared.infrastructure.bus.query import InMemoryQueryBus


def get_event_bus():

    config = configparser.ConfigParser()
    config.read("beer4u/config.ini")

    return RabbitMQEventBus(
        domain="server",
        host=config.get("rabbitmq", "host"),
        port=config.getint("rabbitmq", "port"),
        username=config.get("rabbitmq", "user"),
        password=config.get("rabbitmq", "pass"),
    )


def get_query_bus():
    return InMemoryQueryBus()


def get_command_bus():
    return InMemoryCommandBus()
