"""
Evitando ogni meccanismo di login,
creare un db dove salvare i prodotti:
- codice numerico univoco autoincrementale
- nome
- prezzo
Creare poi un meccanismo basato sui coockie
per salvare localmente al device il nostro carrello
della spesa.
Nel carrello uno stesso prodotto non può essere ripetuto
più volte ma deve avere quantità = 2+
ROUTE 1: aggiunge prodotti al database
ROUTE 2: elimina prodotti dal database
ROUTE 3: modifica i prodotti nel database
ROUTE 4: aggiunge prodotto al carrello
ROUTE 5: elimina un prodotto dal carrello
ROUTE 6: decrementa la quantità di un prodotto nal carrello

testare accedendo a 127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from httpx import request
from pydantic import BaseModel
import uvicorn
from es04DB import execute, fetchall
import json

app = FastAPI()

class Prodotto(BaseModel):
  id:int = None
  nome:str = None
  prezzo:float = None

class DeleteProdotto(BaseModel):
  id:int = None
  nome:str = None

class UpdateProdotto(BaseModel):
  id:int = None
  nome:str = None
  prezzo:float = None

@app.get("/")

@app.post("/prodotto")
def post_prodotto(prodotto:Prodotto):
  query = """
    insert into Prodotti(nome,prezzo)
    values(%s,%s)
    """
  execute(query,
    (prodotto.nome, prodotto.prezzo)
  )
  return True

@app.delete("/prodotto")
def delete_prodotto(prodotto:DeleteProdotto):
  if prodotto.id != None:
    query = "delete from Prodotti where id = %s"
    execute(query, (prodotto.id,))
  elif prodotto.nome != None:
    query = "delete from Prodotti where nome = %s"
    execute(query, (prodotto.nome,))
  else:
    raise HTTPException(422, "Prodotto non identificabile")
  return True

@app.patch("/prodotto")
def patch_prodotto(prodotto:UpdateProdotto):
    if prodotto.id != None:
        if prodotto.prezzo != None and prodotto.nome != None:
            query = "update Prodotti set prezzo = %s , nome = %s where id = %s"
            execute(query, (prodotto.prezzo, prodotto.nome, prodotto.id))
        elif prodotto.prezzo != None:
            query = "update Prodotti set prezzo = %s where id = %s"
            execute(query, (prodotto.prezzo, prodotto.id))
        elif prodotto.nome != None:
            query = "update Prodotti set nome = %s where id = %s"
            execute(query, (prodotto.nome, prodotto.id))
        else:
            raise HTTPException(422, "Prodotto non modificabile")
    elif prodotto.nome != None and prodotto.prezzo != None:
        query = "update Prodotti set prezzo = %s where nome = %s"
        execute(query, (prodotto.prezzo, prodotto.nome))
    else:
        raise HTTPException(422, "Prodotto non modificabile")
    
@app.post("/carrello")
def post_carrello(prodotto:Prodotto, request:Request):
    carrello:str = request.cookies.get("carrello", "{}")
    carrello : dict = json.loads(carrello)
    id = str(prodotto.id)
    if id not in carrello:
       carrello[id] = { "prodotto": prodotto.model_dump(), "quantita": 1 }
    else: 
       x = carrello[id]
       x["quantita"] += 1
       carrello[id] = x
       # carrello[id]["quantità"] += 1
       
    resp = JSONResponse(carrello)
    resp.set_cookie("carrello", json.dumps(carrello))
    return resp 

@app.get("/checkout")
def checkout():
    carrello:str = request.cookies.get("carrello", "{}")
    carrello : dict = json.loads(carrello)
    elenco = tuple(carrello.keys())
    query = f"""select * from prodotti where id in {elenco} """
    prodotti = fetchall(query)
    for x in prodotti:
        id = str( x["id"])
        carrello[id]["prodotto"] = x
    
    carrello_new = {}
    for x in prodotti:
       id = str(x["id"])
       carrello [id]["prodotto"] = x
       carrello_new[id] = carrello[id]
    return carrello


uvicorn.run(app)




