from fastapi import APIRouter, Query
from pydantic import Json

from src.contexts.beer.store.application.command import (
    DeleteStoreCommand,
    RegisterStoreCommand,
    UpdateStoreCommand,
)
from src.contexts.beer.store.application.query import (
    FindStoreByIdQuery,
    SearchStoreByCriteriaQuery,
)
from src.contexts.beer.store.domain.store import Store
from src.contexts.shared.domain.bus.command import CommandBus
from src.contexts.shared.domain.bus.query import QueryBus

from ..dependecy_injection.container import container
from ..schemas.common import MessageResponseSchema
from ..schemas.store import RegisterStoreSchema, StoreSchema, UpdateStoreSchema

router = APIRouter(prefix="/stores", tags=["Stores"])
query_bus: QueryBus = container.get("QueryBus")
command_bus: CommandBus = container.get("CommandBus")


@router.get("", response_model=list[StoreSchema])
async def search_by_criteria(
    filter: Json = Query(None),
    sort: Json = Query(None),
    page_size: int = Query(default=100),
    page_number: int = Query(default=1),
):
    query = SearchStoreByCriteriaQuery(filter, sort, page_size, page_number)
    stores: list[Store] = query_bus.ask(query)
    return [store.to_primitives() for store in stores]


@router.get("/{id}", response_model=StoreSchema)
async def get_store(id: str):
    query = FindStoreByIdQuery(id)
    store: Store = query_bus.ask(query)
    return store.to_primitives()


@router.post("")
async def register_store(store: RegisterStoreSchema):
    command = RegisterStoreCommand(
        store.name, store.address.model_dump(), store.phone
    )
    command_bus.dispatch(command)
    return {"message": "Store registered"}


@router.put("/{id}")
async def update_store(id: str, store: UpdateStoreSchema):
    command = UpdateStoreCommand(
        id,
        store.name,
        store.address.model_dump(),
        store.phone,
        store.discarded,
    )
    command_bus.dispatch(command)
    return {"message": "Store updated"}


@router.delete("/{id}", response_model=MessageResponseSchema)
async def delete_store(id: str):
    command = DeleteStoreCommand(id)
    command_bus.dispatch(command)
    return {"message": "Store deleted"}
