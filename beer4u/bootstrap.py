from beer4u.beer.beer.application.command import (
    DeleteBeerCommandHandler,
    RegisterBeerCommandHandler,
    UpdateBeerCommandHandler,
)
from beer4u.beer.beer.application.query import (
    FindBeerByIdQueryHandler,
    SearchAllBeerQueryHandler,
)
from beer4u.beer.beer.infrastructure.persistence.sqlite import (
    SqliteBeerRepository,
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
from beer4u.beer.store.infrastructure.persistence.sqlite import (
    SqliteStoreRepository,
)
from beer4u.ioc_container import IoCContainer
from beer4u.shared.infrastructure.bus.command.in_memory_command_bus import (
    InMemoryCommandBus,
)
from beer4u.shared.infrastructure.bus.query.in_memory_query_bus import (
    InMemoryQueryBus,
)
from beer4u.shared.infrastructure.persistence.sqlite.db import SqliteSession


def bootstrap() -> IoCContainer:
    ioc_container = IoCContainer()

    ioc_container.register("session", SqliteSession)
    ioc_container.register("BeerRepository", SqliteBeerRepository)
    ioc_container.register("StoreRepository", SqliteStoreRepository)
    ioc_container.register(
        "command_handlers",
        [
            RegisterBeerCommandHandler,
            UpdateBeerCommandHandler,
            DeleteBeerCommandHandler,
            RegisterStoreCommandHandler,
            UpdateStoreCommandHandler,
            DeleteStoreCommandHandler,
        ],
    )
    ioc_container.register(
        "query_handlers",
        [
            FindBeerByIdQueryHandler,
            SearchAllBeerQueryHandler,
            FindStoreByIdQueryHandler,
            SearchAllStoreQueryHandler,
        ],
    )
    ioc_container.register("CommandBus", InMemoryCommandBus)
    ioc_container.register("QueryBus", InMemoryQueryBus)

    return ioc_container
