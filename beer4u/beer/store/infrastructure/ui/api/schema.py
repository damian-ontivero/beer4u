from pydantic import BaseModel


class AddressSchema(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


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
