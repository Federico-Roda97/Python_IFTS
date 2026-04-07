"""
Chiedere in input una lunghezza in qualsiasi unità di misura: 10Km e convertirla in metri
"""

def estrai_numero_unita(input_str):
    """Estrae numero e unità da una stringa come '10Km'."""
    i = 0
    while i < len(input_str) and (input_str[i].isdigit() or input_str[i] == '.'):
        i += 1
    numero = float(input_str[:i])
    unita = input_str[i:].strip().lower()
    return numero, unita

def converti_in_metri(numero, unita):
    """Converte una lunghezza da unità note in metri."""
    conversioni = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'dm': 0.1,
        'hm': 100
    }
    
    if unita not in conversioni:
        print(f"Unità '{unita}' non riconosciuta!")
        return None
    
    return numero * conversioni[unita]

# Main
input_utente = input("Inserisci una lunghezza (es: 10Km, 500m, 25cm): ")
numero, unita = estrai_numero_unita(input_utente)
metri = converti_in_metri(numero, unita)

if metri is not None:
    print(f"{numero} {unita.upper()} = {metri} metri")

