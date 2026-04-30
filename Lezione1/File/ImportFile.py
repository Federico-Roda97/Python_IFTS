import os
print(os.getcwd())
file = open("Python_IFTS/Lezione1/Dizionari/EsDizionari.py")
content = file.read()
c = content.count("conteggio")
print(c, len(content))