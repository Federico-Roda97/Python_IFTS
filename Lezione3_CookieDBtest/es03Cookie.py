from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

class User(BaseModel):
    username:str
    password:str


app = FastAPI()

@app.post("/login")
def login(user:User):
    if user.username == "admin" and user.password == "admin":
        resp = JSONResponse(True, 200)
        resp.set_cookie("auth" , "abcdefgh", 120) #token di autenticazione
        return resp
    
    raise HTTPException(401, "Credenziali Errate")

@app.get("/segreto")
def segreto(request:Request):
    if request.cookies.get("auth") != "abcdefgh":
        raise HTTPException(401, "Credenziali Errate")
    return "Carlo mangia prima di pranzo"


@app.get("/logout")
def logout():
    resp = JSONResponse(True,200)
    resp.delete_cookie("auth")
    return resp
    


uvicorn.run(app)