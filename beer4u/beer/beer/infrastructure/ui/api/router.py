from fastapi import APIRouter, Query
from pydantic import Json

from beer4u.beer.beer.application.command import (
    DeleteBeerCommand,
    RegisterBeerCommand,
    UpdateBeerCommand,
)
from beer4u.beer.beer.application.query import (
    FindBeerByIdQuery,
    SearchBeerByCriteriaQuery,
)
from beer4u.shared.domain.bus.command import CommandBus
from beer4u.shared.domain.bus.query import QueryBus
from beer4u.shared.infrastructure.ui.api.v1.bootstrap import bootstrap
from beer4u.shared.infrastructure.ui.api.v1.schema import MessageResponseSchema

from .schema import BeerSchema, RegisterBeerSchema, UpdateBeerSchema

router = APIRouter(prefix="/beers", tags=["Beers"])

ioc_container = bootstrap()
query_bus: QueryBus = ioc_container.resolve("query_bus")
command_bus: CommandBus = ioc_container.resolve("command_bus")


@router.get("", response_model=list[BeerSchema])
async def search_by_criteria(
    filter: Json = Query(None),
    sort: Json = Query(None),
    page_size: int = Query(default=100),
    page_number: int = Query(default=1),
):
    query = SearchBeerByCriteriaQuery(filter, sort, page_size, page_number)
    result = query_bus.ask(query)
    return [beer.to_primitives() for beer in result]


@router.get("/{id}", response_model=BeerSchema)
async def search(id: str):
    query = FindBeerByIdQuery(id)
    result = query_bus.ask(query)
    return result.to_primitives()


@router.post("")
async def register(beer: RegisterBeerSchema):
    command = RegisterBeerCommand(
        beer.name, beer.type, beer.alcohol, beer.description
    )
    command_bus.dispatch(command)
    return {"message": "Beer registered"}


@router.put("/{id}")
async def update(id: str, beer: UpdateBeerSchema):
    command = UpdateBeerCommand(
        id, beer.name, beer.type, beer.alcohol, beer.description
    )
    command_bus.dispatch(command)
    return {"message": "Beer updated"}


@router.delete("/{id}", response_model=MessageResponseSchema)
async def delete(id: str):
    command = DeleteBeerCommand(id)
    command_bus.dispatch(command)
    return {"message": "Beer deleted"}
