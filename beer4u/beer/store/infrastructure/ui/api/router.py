from fastapi import APIRouter, Depends

from beer4u.beer.store.application.command.delete_command import (
    DeleteStoreCommand,
)
from beer4u.beer.store.application.command.register_command import (
    RegisterStoreCommand,
)
from beer4u.beer.store.application.command.update_command import (
    UpdateStoreCommand,
)
from beer4u.beer.store.application.query.search_all_query import (
    SearchAllStoreQuery,
)
from beer4u.beer.store.application.query.search_by_id_query import (
    SearchStoreByIdQuery,
)
from beer4u.beer.store.infrastructure.ui.api.schema import (
    RegisterStoreSchema,
    StoreSchema,
    UpdateStoreSchema,
)
from beer4u.shared.domain.bus.command.command_bus import CommandBus
from beer4u.shared.domain.bus.query.query_bus import QueryBus
from beer4u.shared.infrastructure.ui.api.v1.dependency import (
    get_command_bus,
    get_query_bus,
)
from beer4u.shared.infrastructure.ui.api.v1.schema import MessageResponseSchema

router = APIRouter(prefix="/stores", tags=["Stores"])


@router.get("", response_model=list[StoreSchema])
async def list_all_stores(
    query_bus: QueryBus = Depends(get_query_bus),
):
    query = SearchAllStoreQuery()
    result = query_bus.ask(query)
    return [store.to_primitives() for store in result]


@router.get("/{id}", response_model=StoreSchema)
async def get_store(
    id: str,
    query_bus: QueryBus = Depends(get_query_bus),
):
    query = SearchStoreByIdQuery(id)
    result = query_bus.ask(query)
    return result.to_primitives()


@router.post("")
async def register_store(
    store: RegisterStoreSchema,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = RegisterStoreCommand(
        store.name, store.address.model_dump(), store.phone
    )
    return command_bus.dispatch(command)


@router.put("/{id}")
async def update_store(
    id: str,
    store: UpdateStoreSchema,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = UpdateStoreCommand(
        id,
        store.name,
        store.address.model_dump(),
        store.phone,
        store.discarded,
    )
    return command_bus.dispatch(command)


@router.delete("/{id}", response_model=MessageResponseSchema)
async def delete_store(
    id: str,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = DeleteStoreCommand(id)
    command_bus.dispatch(command)
    return {"message": "Store deleted"}
