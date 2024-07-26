import requests

def test_should_get_list_of_products():
    r = requests.get('http://localhost:8000/products')
    response = r.json()
    print(response)

test_should_get_list_of_products()

"""from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_should_get_list_of_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)"""