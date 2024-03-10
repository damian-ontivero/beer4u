from pydantic import BaseModel


class AddressSchema(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
