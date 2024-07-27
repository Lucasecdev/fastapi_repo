from fastapi import FastAPI
from json_db import JsonDB
from product import Product


app = FastAPI()

productDB = JsonDB(path='./data/products.json')


@app.get("/products")


def get_products():  # noqa: E304
    products = productDB.read()
    return {"products": products}


@app.post("/products")


def create_product(product: Product):  # noqa: E304

    productDB.insert(product)

    return {"status": "inserted"}
