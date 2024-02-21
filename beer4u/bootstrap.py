import configparser

from beer4u.beer.beer.application.command import (
    DeleteBeerCommandHandler,
    RegisterBeerCommandHandler,
    UpdateBeerCommandHandler,
)
from beer4u.beer.beer.application.query import (
    FindBeerByIdQueryHandler,
    SearchAllBeerQueryHandler,
)
from beer4u.beer.store.application.command import (
    DeleteStoreCommandHandler,
    RegisterStoreCommandHandler,
    UpdateStoreCommandHandler,
)
from beer4u.beer.store.application.query import (
    FindStoreByIdQueryHandler,
    SearchAllStoreQueryHandler,
)
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
    for handler in QUERY_HANDLERS:
        InMemoryQueryBus().register(handler.subscribe_to, handler)
    return InMemoryQueryBus()


def get_command_bus():
    for handler in COMMAND_HANDLERS:
        InMemoryCommandBus().register(handler.subscribe_to, handler)
    return InMemoryCommandBus()
