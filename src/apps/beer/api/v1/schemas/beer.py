from pydantic import BaseModel


class BeerSchema(BaseModel):
    id: str
    name: str
    type: str
    alcohol: float
    description: str
    discarded: bool


class RegisterBeerSchema(BaseModel):
    name: str
    type: str
    alcohol: float
    description: str


class UpdateBeerSchema(BaseModel):
    name: str
    type: str
    alcohol: float
    description: str
    discarded: bool
