from concurrent.futures import process
from time import process_time
from urllib import response
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
app = FastAPI()


app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def hello():
    return {"message": "Hello World"}