from ast import Param
from msilib.schema import Class
from turtle import update
from typing import Any, Optional, Dict
from urllib import response
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import uvicorn
app = FastAPI()

items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})

#class로 주입.
class ClassParams:
    def __init__(
        self, q:Optional[str] = None, offset:int = 0, limit: int = 100):

        self.q = q
        self.offset = offset
        self.limit = limit

@app.get("/items/class")
async def get_item_with_class(params: ClassParams = Depends(ClassParams)):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response

#pydantic으로 주입
class PydanticParams(BaseModel):
    q: Optional[str] = Field(None, min_length=2)
    offset: int = Field(0, ge=0)
    limit: int = Field(100, gt=0)

@app.get("/item/pydantic")
async def get_items_with_pydantic(params: PydanticParams = Depends()):
    response = {}
    if params.q:
        response.update({"q": params.q})
    
    result = items[params.offset: params.offset + params.limit]
    response.update({"items":result})

    return response

# DI로 주입

async def get_q(q: Optional[str] = None) -> Optional[str]:
    return q

async def func_params_with_sub(
    q: Optional[str] = Depends(get_q), offset: int = 0, limit: int = 100) -> Dict[str, Any]:
    return {"q":q, "offset":offset, "limit":limit}


@app.get("/items/func/sub")
async def get_items_with_func_sub(params: dict = Depends(func_params_with_sub)):
    response = {}
    if params["q"]:
        response.update({"q": params["q"]})

    result = items[params["offset"]: params["offset"] + params["limit"]]  #슬라이싱
    response.update({"items":result})

    return response