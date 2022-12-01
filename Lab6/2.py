'''Napisz funkcje oblicz(), która ma dwa parametry i oblicza ich sumę oraz różnicę. Ponadto zwraca
jednocześnie jak wynik dodawania, tak i odejmowania.'''

def oblicz(a,b):
    suma = a+b
    roznica = a-b
    return suma, roznica

print(oblicz(15,5))         #krotka

x, y = oblicz(3,2)
print(f"Suma = {x}, Różnica  = {y}")