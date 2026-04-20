from fastapi import FastAPI  
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn 

app = FastAPI()

@app.get("/")
def index():
    return FileResponse("Lezione3_CookieDBtest/static/index.html")

app.mount("/", StaticFiles(directory="Lezione3_CookieDBtest/static"))

uvicorn.run(app)

