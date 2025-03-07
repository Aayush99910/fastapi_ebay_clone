from fastapi import FastAPI # type: ignore
from datetime import date 
app = FastAPI()

# fake data that we are going to use for now
fake_database = {
	1: {
      "name": "Iphone 11", 
      "price": 1500, 
      "year": 2018, 
      "quality": "fair", 
      "seller": "Aayush", 
      "posted_date": date(2025, 3, 7)
  },
	2: {
      "name": "Toyota Accord", 
      "price": 15000, 
      "year": 2024, 
      "quality": "brand new", 
      "seller": "Shayan", 
      "posted_date": date(2025, 2, 14)
  }
}

@app.get("/")
async def home_page():
  return {"message": "Welcome to our application!"}


@app.get("/allproducts")
async def show_items():
  return {"Items": fake_database}

