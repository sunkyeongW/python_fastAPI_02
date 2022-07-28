from email import message
import time

from typing import Optional
from fastapi import BackgroundTasks, Depends, FastAPI, status
from sympy import N

app = FastAPI()

def write_log(message: str):
    time.sleep(2.0)

    with open("log.txt", mode="a") as log:
        log.write(message)

#의존성 주입에서 사용
def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}", status_code=status.HTTP_202_ACCEPTED)
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)

    return {"message": "message sent"}