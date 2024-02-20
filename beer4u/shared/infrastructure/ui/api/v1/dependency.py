import configparser

from beer4u.shared.infrastructure.bus.command import InMemoryCommandBus
from beer4u.shared.infrastructure.bus.event import RabbitMQEventBus
from beer4u.shared.infrastructure.bus.query import InMemoryQueryBus

config = configparser.ConfigParser()
config.read("beer4u/config.ini")

rabbitmq_host = config.get("rabbitmq", "host")
rabbitmq_port = config.getint("rabbitmq", "port")
rabbitmq_user = config.get("rabbitmq", "user")
rabbitmq_pass = config.get("rabbitmq", "pass")


def get_rabbitmq_event_bus():
    return RabbitMQEventBus(
        domain="server",
        host=rabbitmq_host,
        port=rabbitmq_port,
        username=rabbitmq_user,
        password=rabbitmq_pass,
    )


def get_query_bus():
    return InMemoryQueryBus()


def get_command_bus():
    return InMemoryCommandBus()
