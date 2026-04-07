"""
Chiedere in input all'utente i prodotti he vuole comprare
Terminare la richiesta alla prima immisione vuota
Contare per ogni prodottto quante volte è stato inserito
"""

lista = []
conteggio = {}
while True:
    prodotto = input("Prodotto [vuoto per terminare]: ")
    if prodotto == "":
        break
    lista.append(prodotto)
    if prodotto not in conteggio:
        conteggio[prodotto] = 1
    else:
        conteggio[prodotto] += 1

print("il carrello è:",lista)
print("il conteggio è:",conteggio)