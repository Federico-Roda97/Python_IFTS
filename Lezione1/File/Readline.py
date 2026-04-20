file = open("Python_IFTS/Lezione1/Dizionari/EsDizionari.py")

c = 0
while True:
    content = file.readline()
    if len(content) == 0:
        break
    c +=content.count("conteggio")

print(c)