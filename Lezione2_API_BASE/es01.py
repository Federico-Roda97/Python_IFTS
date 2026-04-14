from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return "Ciao da Federico"

@app.get("/lista")
def lista():
    return[1,2,3,4,5,6,7]

@app.get("/file")
def file():
    f = open("Lezione1/Dizionari/Dizionionari.py")
    return f.read()


@app.get("/scrivi")
def scrivi():
    from datetime import datetime
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open("Lezione2_API_BASE/f01.txt", "w")
    f.write(data)
    return data


@app.get("/log", response_class=PlainTextResponse)
def log():
    
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Lezione2_API_BASE/f02.txt", "a") as f:
        f.write(data + "\n")

    with open("Lezione2_API_BASE/f02.txt", "r") as f:
        return f.read()



uvicorn.run(app, host="127.0.0.1", port=8000)

