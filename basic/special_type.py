from fastapi import FastAPI, Cookie, Header
app = FastAPI()


@app.get('/')
async def cookie_and_headers(cookie: str = Cookie(None), accept: str = Header(None)):
    """
    if you want cookie or header, use Cookie or Header as Query
    """
    return {"text": f"hello world, {cookie}, {accept}!"}
