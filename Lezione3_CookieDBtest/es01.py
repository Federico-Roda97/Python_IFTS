from fastapi import FastAPI  #gestisce HTTP
from fastapi import HTTPException
from pydantic import BaseModel #tipizzazione python
import uvicorn # gestisce TCP
from datetime import date

class Persona(BaseModel):
    nome:str
    cognome:str
    sesso:str
    data:date

app = FastAPI()

def extract_3_consonants(x:str):
    y = ""
    i = 0 
    for c in x:
        if i < 3 and c.lower not in "aeiou":
            y += c
            i += 1
    
    for c in x:
        if i < 3 and c.lower in "aeiou":
            y += c
            i += 1
    return y


monthMap = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]

@app.post("/cf")
def cf(user:Persona):
    if user.sesso not in ["M", "F"]:
        raise HTTPException(409, "Sesso per CF must be M or F")
    
    CF = extract_3_consonants(user.cognome)
    CF += extract_3_consonants(user.nome)

    d = user.data.day + (40 if user.sesso == "F" else 0)
    m = user.data.month
    y = user.data.year

    CF += "%02d" % (y % 100)
    CF += monthMap[m-1]
    CF += "%02d" % (d) 

# il sesso si codifica sommando al giorno di nascita 40 se F, 0 se M
    
    return CF

uvicorn.run(app)