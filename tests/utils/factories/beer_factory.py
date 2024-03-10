import factory

from beer4u.beer.beer.domain.beer import Beer
from tests.utils.factories.entity_id_factory import EntityIdFactory


class BeerFactory(factory.Factory):
    class Meta:
        model = Beer

    id = factory.SubFactory(EntityIdFactory)
    name = factory.Faker("name")
    type = factory.Faker("word")
    alcohol = factory.Faker("random_number", digits=2)
    description = factory.Faker("text")
    discarded = False
