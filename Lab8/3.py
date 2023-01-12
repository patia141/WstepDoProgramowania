'''Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.'''

def potega(list1, list2):
    wynik = []
    if len(list1) == len(list2):
        for a in range(len(list1)):
            wynik.append(list1[a]**list2[a])
    return wynik

lista1=[2,3]
lista2=[3,2]
print(potega(lista1,lista2))