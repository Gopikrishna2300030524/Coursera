import pytest
import requests

BASE_URL = "http://localhost:5000/api/products"

def test_create_product():
    response = requests.post(BASE_URL, json={"name": "Test Product", "category": "Test Category", "price": 20, "availability": True})
    assert response.status_code == 201

def test_get_product():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
