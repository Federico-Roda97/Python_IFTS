file = open("src/Lezione1/Dizionari/EsDizionari.py")
content = file.read()
c = content.count("conteggio")
print(c, len(content))