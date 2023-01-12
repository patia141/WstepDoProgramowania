''' Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
wartością – nazwa odpowiedniej funkcji.
Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu.'''

def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b

def dzielenie(a,b):
    if b == 0:
        return None
    else:
        return a/b

dzialanie = {'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}

x = input("Jakie działanie? ")
a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))
print(dzialanie[x](a,b))