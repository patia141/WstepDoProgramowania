'''Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.'''

def zad3(*args):
    print(args)
    for i in args:
        print(i)

def zad3max(liczba1, *args):
    print(*args)
    m = liczba1
    for x in args:
        if x > m:
            m = x
    return m

#zad3(1,1.5,False,[2,3])
print(zad3max(1,33,6,22))
#print(zad3max())