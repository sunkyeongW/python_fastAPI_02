import imp
from urllib.request import Request
from click import File
from fastapi import FastAPI,Form, File, UploadFile, HTTPException
import fastapi
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from tempfile import NamedTemporaryFile
from typing import IO, Any, Optional, Dict   

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name="static")


class SomeError(Exception):
    def __init__(self, name: str, code:int):
        self.name = name
        self.code = code
    
    def __str__(self):
        return f"<{self.name}> is occured. code: <{self.code}>"


class SomeFastAPIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        ) -> None:
        super().__init__(
            status_code=status_code, detail=detail, headers=headers)


app = FastAPI()


@app.get("/fastapierror")
async def get_fastapierror():
    raise SomeFastAPIError(503, "Hello")

@app.exception_handler(SomeError)
async def some_error_handler(request: Request, exc: SomeError):
    return JSONResponse(
        content={"message": f"error is {exc.name}"}, status_code=exc.code)


@app.get("/error")
async def get_error():
    raise SomeError("Hello", 503)


async def save_file(file: IO):
    with NamedTemporaryFile("wb", delete=False) as tempfile:  #delete=True 주의.
        tempfile.write(file.read())
        return tempfile.name  #name:경로


@app.post("/file/store")
async def store_file(file: UploadFile = File(...)):
    path = await save_file(file.file)
    return {"filepath": path}


@app.post("/file/info")
async def get_fileinfo(file: UploadFile = File(...)):
    file_like_obj = file.file 
    contents = await file.read()
    
    return {
        "content_type": file.content_type,
        "filename": file.filename,
        "content" : contents,
    }


@app.post("/file/size")
def get_filesize(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/login")
def login(username:str = Form(...), password:str = Form(...)):
    return {"username":username}


