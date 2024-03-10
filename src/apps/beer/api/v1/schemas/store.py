from pydantic import BaseModel

from .address import AddressSchema


class StoreSchema(BaseModel):
    id: str
    name: str
    address: AddressSchema
    phone: str
    discarded: bool


class RegisterStoreSchema(BaseModel):
    name: str
    address: AddressSchema
    phone: str


class UpdateStoreSchema(BaseModel):
    name: str
    address: AddressSchema
    phone: str
    discarded: bool
