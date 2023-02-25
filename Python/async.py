from typing import Union

import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

async def test_async():
    print("test")
    await asyncio.sleep(5)

async def test_async2():
    print("test2")
    await asyncio.sleep(5)

@app.get("/async/")
async def async_read_root():
    await asyncio.gather(test_async(), test_async2())
    return {"Hello": "World"}