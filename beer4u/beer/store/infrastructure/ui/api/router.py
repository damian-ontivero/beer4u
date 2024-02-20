from fastapi import APIRouter, Depends

from beer4u.beer.store.application.command import (
    DeleteStoreCommand,
    RegisterStoreCommand,
    UpdateStoreCommand,
)
from beer4u.beer.store.application.query import (
    SearchAllStoreQuery,
    SearchStoreByIdQuery,
)
from beer4u.bootstrap import get_command_bus, get_query_bus
from beer4u.shared.domain.bus.command import CommandBus
from beer4u.shared.domain.bus.query import QueryBus
from beer4u.shared.infrastructure.ui.api.v1.schema import MessageResponseSchema

from .schema import RegisterStoreSchema, StoreSchema, UpdateStoreSchema

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
