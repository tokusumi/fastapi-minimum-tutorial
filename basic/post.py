from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional, List
app = FastAPI()


class Data(BaseModel):
    """
    declare types o variables, which is same manner as path/query parameters.
    """
    string: str
    default_none: Optional[int] = None
    lists: List[int]


@app.post('/post')
async def declare_request_body(data: Data):
    """
    requests (POST method):

    - schema that defined in class inherited BaseModel is generated autodoc
    - data is a instance of Data class
    - note: the order is meaningless
    - example of request body:
    ```
    {
        "string": "string",
        "default_none": 0,
        "lists": [1, 2]
    }
    ```
    """
    return {"text": f"hello, {data.string}, {data.default_none}, {data.lists}"}


@app.post('/post/embed')
async def declare_embedded_request_body(data: Data = Body(..., embed=True)):
    """
    requests (POST method):

    - use Body to handle more complex schema
    - if embed=True, the value in request body is converted into variable, if the key of the value matches declared argument.
    - example of request body:
    ```
    {
        "data": {
            "string": "string",
            "default_none": 0,
            "lists": [1, 2]
        }
    }
    ```
    """
    return {"text": f"hello, {data.string}, {data.default_none}, {data.lists}"}


class subDict(BaseModel):
    strings: str
    integer: int


class NestedData(BaseModel):
    """
    use BaseModel type to declare types of nested structure,
    """
    subData: subDict
    subDataList: List[subDict]


@app.post('/post/nested')
async def declare_nested_request_body(data: NestedData):
    """
    requests (POST method):

    - use nested BaseModel type for nested request body
    - if you use arbitrary list or dict, you can use just as List[str], Dict[str, int] or so on.
    - example of request body:
    ```
    {
        "subData": {
            "strings": "string",
            "integer": 0
        },
        "subDataList": [
            {
                "strings": "string",
                "integer": 0
            }
        ]
    }
    ```
    """
    return {"text": f"hello, {data.subData}, {data.subDataList}"}


class ValidatedSubData(BaseModel):
    """
    validation: Use Field
    ex:

    - string: 2 to 5 length and a to b chars is allowed
    - integer: the interger x (1 < x <= 3) is allowed
    """
    strings: str = Field(None, min_length=2, max_length=5, regex=r'[a-b]+.')
    integer: int = Field(..., gt=1, le=3)  # required


class ValidatedNestedData(BaseModel):
    """
    use BaseModel type to declare types of nested structure,
    """
    subData: ValidatedSubData = Field(..., example={"strings": "aaa", "integer": 2})
    subDataList: List[ValidatedSubData] = Field(..., example=[{"strings": "aaa", "integer": 2}, {
        "strings": "bbb", "integer": 3}])


@app.post('/validation')
async def validation(data: ValidatedNestedData):
    """
    requests (validation):

    - validation for values of request body uses Field
    - you can set example in Body or Field
    """
    return {"text": f"hello, {data.subData}, {data.subDataList}"}
