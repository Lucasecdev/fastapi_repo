import requests
import time


def test_should_get_list_of_products():

    r = requests.get('http://localhost:8000/products')
    response = r.json()
    print(response)


test_should_get_list_of_products()


def test_should_get_list_of_products():
    time.sleep(10)  # Espera 10 segundos antes de tentar acessar a API
    r = requests.get('http://localhost:8000/products')
    assert r.status_code == 200
