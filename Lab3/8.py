'''Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *'''

x = int(input("podaj liczbę: "))
for i in range(x):
    print("*" * x)