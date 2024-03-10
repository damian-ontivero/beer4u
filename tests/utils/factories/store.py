import factory

from src.contexts.beer.store.domain.store import Store
from tests.utils.factories.address import AddressFactory
from tests.utils.factories.entity_id import EntityIdFactory


class StoreFactory(factory.Factory):
    class Meta:
        model = Store

    id = factory.SubFactory(EntityIdFactory)
    name = factory.Faker("name")
    address = factory.SubFactory(AddressFactory)
    phone = factory.Faker("phone_number")
    discarded = False
