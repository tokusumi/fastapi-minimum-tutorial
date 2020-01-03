from fastapi import FastAPI, Query, Path
from typing import Optional
app = FastAPI()


@app.get('/get/{path}')
async def path_and_query_params(path: str, query: int, default_none: Optional[str] = None):
    """
    requests (GET method):

    - path parameters: declare variable in url and arguments
    - query parametes: declare variable in only arguments
    - if you declare python type hint, autodoc is created and the type of arguments is to be what you declared
    - if you declare default value, you can access default value. if no default value, then the parameters is required
    - note: the order is meaningless
    """
    assert isinstance(path, str)
    assert isinstance(query, int)
    return {"text": f"hello, {path}, {query} and {default_none}"}


@app.get('/validation/{path}')
async def validation(
        string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
        integer: int = Query(..., gt=1, le=3),  # required
        alias_query: str = Query('default', alias='alias-query'),
        path: int = Path(10)):
    """
    requests (validation):

    - validation for query parameters uses Query
    - validation for path parameters uses Path
    - first arguments means default value. if set ..., the parameters is required.
    - alias: different name between argument in python and request parameters is allowed
    - example of validation:
        - string: 2 to 5 length and a to c chars is allowed
        - integer: the interger x (1 < x <= 3) is allowed
    - if validation error occured, return as follows:
        ```
        {
        "detail": [
            {
            "loc": [
                "body",
                "data",
                "string"
            ],
            "msg": "ensure this value has at most 5 characters",
            "type": "value_error.any_str.max_length",
            "ctx": {
                "limit_value": 5
            }
            }
        ]
        }
        ```
    """
    return {"string": string, "integer": integer, "alias-query": alias_query, "path": path}
