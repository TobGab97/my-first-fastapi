from typing import List
from fastapi import FastAPI
from models import *
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi"}

@app.get("/stocks", response_model=List[Stock_Pydantic])
async def get_stocks():
    return await Stock_Pydantic.from_queryset(Stocks.all())


@app.post("/stocks", response_model=Stock_Pydantic)
async def create_stock(Stock: StockIn_Pydantic):
    stock_obj = await Stocks.create(**Stock.dict(exclude_unset=True))
    return await Stock_Pydantic.from_tortoise_orm(stock_obj)


register_tortoise(
    app,
    db_url="postgres://uzytk:haslo@db:5432/root",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)