from typing import Union
from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()

auth_router = APIRouter(prefix="/users", tags=["users"])


@app.get("/", summary="Main page", tags=["Main routes"])
async def read_root():
    """
    Main route that returns a greeting message.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}", summary="Get item", tags=["Elements"])
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Get information about an item by its ID.

    - **item_id**: ID of the item (required parameter).
    - **q**: Additional query parameter (optional).

    """
    return {"item_id": item_id, "q": q}


@app.get("/items/", summary="Get all items", tags=["Elements"])
async def read_items():
    """
    Get a list of all items.
    """
    return {"message": "This is a list of all items"}


@app.get("/hello/{name}", summary="Greet user", tags=["Main routes"])
async def greet_user(name: str):
    """
    Greet the user by name.

    - **name**: The user's name (required parameter).
    """
    return {"message": f"Hello, {name}!"}


def main():
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
