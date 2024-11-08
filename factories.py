from factory import Factory, Faker
from myapp.models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product
    name = Faker('word')
    category = Faker('word')
    price = Faker('random_int', min=10, max=100)
    availability = Faker('boolean')
