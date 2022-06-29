from fastapi import APIRouter
from pydantic import BaseModel
from ..models.testModel import Test

router = APIRouter()

@router.get("/test")
async def get_test():
    test1 = Test("test")
    return test1