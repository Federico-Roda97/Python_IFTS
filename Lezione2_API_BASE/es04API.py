from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import uvicorn

class Data1(BaseModel):
    nome:str
    eta:int
    altezza:float


app = FastAPI()

@app.post("/post1")
def post1(data:Data1):

    print(data)
    return data



class Data2(BaseModel):
    nome:str
    eta:int = 0
    genere:str
    altezza:float

# verifica accesso in discoteca

@app.post("/post2")
def post2(data:Data2):
    # se il genere è femmina permetti, l'accesso sopra i 16 anni
    if "f" == data.genere[0].lower() and data.eta >= 16:
        return JSONResponse(data.model_dump(), 202)
    
    # se il genere è maschio l'età deve essere >=18 e l'altezza >=183
    if "m" == data.genere[0].lower() and data.eta >= 18 and data.altezza >= 183:
        return JSONResponse(data.model_dump(), 202)
    
    # se non binario l'altezza deve essere minore di 2.5 metri
    if data.genere[0].lower() != "m" and data.genere[0].lower() != "f" and data.altezza < 250 and data.eta >= 18:
        return JSONResponse(data.model_dump(), 202)
    
    # se si sta fuori, l'app deve ritornare codice http 406 Not Accettable
    return JSONResponse(data.model_dump(), 406)

uvicorn.run(app)