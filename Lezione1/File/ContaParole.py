# Conta le parole in un file e restituisce un dizionario con la parola e il numero di occorrenze
file = open("Lezione1/Dizionari/EsDizionari.py")

c = {}
while True:
    content = file.readline()
    if len(content) == 0:
        break
    parole = content.split()
    for p in parole:
        p = p.lower()
        p= p.replace('"',"")
        p= p.replace("'", "")
        if p in c:
            c[p] += 1
        else:
            c[p] = 1

out = open("Lezione1/File/ContaParoleReport.csv", "w")

out.write("Parola, conteggio\n")
for key in c:
    out.write(f"{key}:{c[key]}\n")

print(c)