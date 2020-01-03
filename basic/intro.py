from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    """
    autodoc:

    - access http://127.0.0.1:8000/docs, swagger UI is created automatically.
    """
    return {"text": "hello world!"}
