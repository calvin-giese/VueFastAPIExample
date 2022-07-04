from fastapi import APIRouter
from pydantic import BaseModel
from ..models.Item import Item

router = APIRouter()

@router.get("/item")
async def get_item():
    item1 = Item("item")
    return item1