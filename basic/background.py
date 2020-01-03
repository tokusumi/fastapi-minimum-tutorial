from fastapi import BackgroundTasks, FastAPI
from time import sleep
from datetime import datetime

app = FastAPI()


def time_bomb(count: int):
    sleep(count)
    print(f'bomb!!! {datetime.utcnow()}')


@app.get('/{count}')
async def back(count: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(time_bomb, count)
    return {"text": "finish"}
