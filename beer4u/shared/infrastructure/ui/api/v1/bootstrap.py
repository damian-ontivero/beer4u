from beer4u.beer.beer.application.command import BEER_COMMAND_HANDLERS
from beer4u.beer.beer.application.query import BEER_QUERY_HANDLERS
from beer4u.beer.beer.infrastructure.persistence.sqlite import (
    SqliteBeerRepository,
)
from beer4u.beer.store.application.command import STORE_COMMAND_HANDLERS
from beer4u.beer.store.application.query import STORE_QUERY_HANDLERS
from beer4u.beer.store.infrastructure.persistence.sqlite import (
    SqliteStoreRepository,
)
from beer4u.ioc_container import IoCContainer
from beer4u.shared.infrastructure.bus.command import InMemoryCommandBus
from beer4u.shared.infrastructure.bus.query import InMemoryQueryBus
from beer4u.shared.infrastructure.persistence.sqlite.db import SqliteSession


def bootstrap() -> IoCContainer:
    ioc_container = IoCContainer()

    # Register repositories
    ioc_container.register(
        "beer_repository", SqliteBeerRepository(SqliteSession)
    )
    ioc_container.register(
        "store_repository", SqliteStoreRepository(SqliteSession)
    )

    # Register query handler map
    ioc_container.register(
        "query_handler_map",
        {
            **{
                query: handler(ioc_container.resolve("beer_repository"))
                for query, handler in BEER_QUERY_HANDLERS.items()
            },
            **{
                query: handler(ioc_container.resolve("store_repository"))
                for query, handler in STORE_QUERY_HANDLERS.items()
            },
        },
    )

    # Register query bus
    ioc_container.register(
        "query_bus",
        InMemoryQueryBus(ioc_container.resolve("query_handler_map")),
    )

    # Register command handler map
    ioc_container.register(
        "command_handler_map",
        {
            **{
                command: handler(ioc_container.resolve("beer_repository"))
                for command, handler in BEER_COMMAND_HANDLERS.items()
            },
            **{
                command: handler(ioc_container.resolve("store_repository"))
                for command, handler in STORE_COMMAND_HANDLERS.items()
            },
        },
    )

    # Register command bus
    ioc_container.register(
        "command_bus",
        InMemoryCommandBus(ioc_container.resolve("command_handler_map")),
    )

    return ioc_container
