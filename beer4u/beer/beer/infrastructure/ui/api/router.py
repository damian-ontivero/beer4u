from fastapi import APIRouter, Depends

from beer4u.beer.beer.application.command import (
    DeleteBeerCommand,
    RegisterBeerCommand,
    UpdateBeerCommand,
)
from beer4u.beer.beer.application.query import (
    FindBeerByIdQuery,
    SearchAllBeerQuery,
)
from beer4u.bootstrap import get_command_bus, get_query_bus
from beer4u.shared.domain.bus.command import CommandBus
from beer4u.shared.domain.bus.query import QueryBus
from beer4u.shared.infrastructure.ui.api.v1.schema import MessageResponseSchema

from .schema import BeerSchema, RegisterBeerSchema, UpdateBeerSchema

router = APIRouter(prefix="/beers", tags=["Beers"])


@router.get("", response_model=list[BeerSchema])
async def list_all_beers(
    query_bus: QueryBus = Depends(get_query_bus),
):
    query = SearchAllBeerQuery()
    result = query_bus.ask(query)
    return [beer.to_primitives() for beer in result]


@router.get("/{id}", response_model=BeerSchema)
async def get_beer(
    id: str,
    query_bus: QueryBus = Depends(get_query_bus),
):
    query = FindBeerByIdQuery(id)
    result = query_bus.ask(query)
    return result.to_primitives()


@router.post("")
async def register_beer(
    beer: RegisterBeerSchema,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = RegisterBeerCommand(
        beer.name, beer.type, beer.alcohol, beer.description
    )
    return command_bus.dispatch(command)


@router.put("/{id}")
async def update_beer(
    id: str,
    beer: UpdateBeerSchema,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = UpdateBeerCommand(
        id, beer.name, beer.type, beer.alcohol, beer.description
    )
    return command_bus.dispatch(command)


@router.delete("/{id}", response_model=MessageResponseSchema)
async def delete_beer(
    id: str,
    command_bus: CommandBus = Depends(get_command_bus),
):
    command = DeleteBeerCommand(id)
    command_bus.dispatch(command)
    return {"message": "Beer deleted"}
