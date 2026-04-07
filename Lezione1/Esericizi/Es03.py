"""
chiedere in input il totale dei minuti lavorati
stampare a video in formato: 11:50 H:m
"""



time = int(input("Inserisci il totale dei minuti lavorati: "))
print (time)

ore = time // 60
minuti = time % 60
print ("ore:" ,ore , "minuti:" ,minuti)

