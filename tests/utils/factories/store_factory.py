import factory

from beer4u.beer.store.domain.store import Store
from beer4u.shared.domain.address import Address


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = factory.Faker("street_name")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zip_code = factory.Faker("zipcode")


class StoreFactory(factory.Factory):
    class Meta:
        model = Store

    id = factory.Faker("uuid4")
    name = factory.Faker("name")
    address = factory.SubFactory(AddressFactory)
    phone = factory.Faker("phone_number")
    discarded = False
