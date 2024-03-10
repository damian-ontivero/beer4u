import factory

from beer4u.shared.domain.entity_id import EntityId


class EntityIdFactory(factory.Factory):
    class Meta:
        model = EntityId

    value = factory.Faker("uuid4")
