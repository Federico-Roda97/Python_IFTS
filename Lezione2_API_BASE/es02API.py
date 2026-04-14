from fastapi import FastAPI, Request
import uvicorn

app= FastAPI()
#http://127.0.0.1:8000/file?fileName=es01.py
#/file?fileName=es01.py
@app.get("/file")
def file(fileName:str):
    "apri, leggi e ritorna un file nella cartella lezione2 con il nome specificato "
    f = open(f"Lezione2_API_BASE/{fileName}")
    return f.read()

@app.get("/file2/{fileName}")
def file2(fileName:str):
    f = open(f"lezione2_API_BASE/{fileName}")
    return f.read()

@app.get("/api/{nome}/{cognome}")
def prova(nome:str, cognome:str):
    return nome+cognome

@app.get("/richiesta")
def richiesta(request:Request):
    print(request.method)
    print(request.base_url)
    return request.query_params
    

uvicorn.run(app)