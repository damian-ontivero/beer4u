import factory

from beer4u.beer.beer.domain.beer import Beer


class BeerFactory(factory.Factory):
    class Meta:
        model = Beer

    id = factory.Faker("uuid4")
    name = factory.Faker("name")
    type = factory.Faker("word")
    alcohol = factory.Faker("random_number", digits=2)
    description = factory.Faker("text")
    discarded = False
