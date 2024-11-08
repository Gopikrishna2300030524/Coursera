import pytest
from myapp.models import Product

def test_create_product():
    product = Product.objects.create(name="Test Product", category="Test Category", price=20, availability=True)
    assert product.id is not None

def test_update_product():
    product = Product.objects.create(name="Test Product", category="Test Category", price=20, availability=True)
    product.name = "Updated Product"
    product.save()
    assert product.name == "Updated Product"

def test_delete_product():
    product = Product.objects.create(name="Test Product", category="Test Category", price=20, availability=True)
    product.delete()
    assert Product.objects.filter(id=product.id).count() == 0
