from fastapi import FastAPI
from models import product
from database import SessionLocal, engine # engine yahan se aayega
import database_models


app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "hellow world"


products = [
    product(id =1, name="Laptop", description="High-performance laptop", price=999.99, quantity=10),
    product(id =2, name="Smartphone", description="Latest Android smartphone", price=699.99, quantity=25),
    product(id =3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50),
    product(id =4, name="Monitor", description="27-inch 4K display", price=329.99, quantity=15),
    product(id =5, name="Keyboard", description="Mechanical RGB keyboard", price=89.99, quantity=40),
    product(id =6, name="Mouse", description="Wireless ergonomic mouse", price=49.99, quantity=60),
]



@app.get("/products")
def read_all_products():
   # db connect karknege 
      # Ye line database se saara data uthayegi
    return db.query(database_models.product).all()


@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/products")
def add_product(product: product):
      products.append(product)
      return product.__dict__
   

@app.put("/products")
def update_product(id : int, product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
        
    return "No product found with the given ID"

@app.delete("/products")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"
        
    return "No product found with the given ID"