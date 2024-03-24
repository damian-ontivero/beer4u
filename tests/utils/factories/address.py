import factory

from src.contexts.shared.domain.address import Address


class AddressFactory(factory.Factory):

    class Meta:
        model = Address

    street = factory.Faker("street_name")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zip_code = factory.Faker("zipcode")
