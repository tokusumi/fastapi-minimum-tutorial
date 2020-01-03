from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED
app = FastAPI()


class ItemOut(BaseModel):
    """
    - declare type of attributes, which is same manner as request body handdling.
    - see post.py for more complex case.
    """
    strings: str
    aux: int = 1
    text: str


@app.get('/', response_model=ItemOut)
async def response(strings: str, integer: int):
    """
    response:

    - declare response structure and set to response_model
    - then, add and delete data to fit with data structure, defined in above class
    """
    return {"text": "hello world!", "strings": strings, "integer": integer}


@app.get('/unset', response_model=ItemOut, response_model_exclude_unset=True)
async def response_exclude_unset(strings: str, integer: int):
    """
    response:

    - response_model_exclude_unset: if True, augumentation of fields is not implemented
    - example:
        "aux" attributes is not returned
    """
    return {"text": "hello world!", "strings": strings, "integer": integer}


@app.get('/exclude', response_model=ItemOut, response_model_exclude={"strings", "aux"})
async def response_exclude(strings: str, integer: int):
    """
    response:

    - response_model_exclude: if assign set of fields name, delete the fields
    - example:
        "aux" and "strings" attributes is not returned
    """
    return {"text": "hello world!", "strings": strings, "integer": integer}


@app.get('/include', response_model=ItemOut, response_model_include={"text"})
async def response_include(strings: str, integer: int):
    """
    response:

    - response_model_include: if assign set of fields name, use only the fields
    - example:
        only "text" attributes is returned
    """
    return {"text": "hello world!", "strings": strings, "integer": integer}


@app.get('/status', status_code=200)
async def response_status_code(integer: int, response: Response):
    """
    response (status code):

    - default status code: set in decorator
    - error handling: use HTTPException
    - set manually: manage startllete explicitly
    """
    if integer > 5:
        # error handling
        raise HTTPException(status_code=404, detail="this is error messages")
    elif integer == 1:
        # set manually
        response.status_code = HTTP_201_CREATED
        return {"text": "hello world, created!"}
    else:
        # default status code
        return {"text": "hello world!"}
