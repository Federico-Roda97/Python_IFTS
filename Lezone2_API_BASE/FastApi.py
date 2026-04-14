from fastapi import FastAPI
import uvicorn


print("inizio")

app = FastAPI()

@app.get("/")
def index():
    return "Ciao da Federico"

uvicorn.run(app, host="127.0.0.1", port=8000)

print("fine")