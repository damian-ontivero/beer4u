import factory

from beer4u.beer.store.domain.store import Store
from tests.utils.factories.address_factory import AddressFactory
from tests.utils.factories.entity_id_factory import EntityIdFactory


class StoreFactory(factory.Factory):
    class Meta:
        model = Store

    id = factory.SubFactory(EntityIdFactory)
    name = factory.Faker("name")
    address = factory.SubFactory(AddressFactory)
    phone = factory.Faker("phone_number")
    discarded = False
