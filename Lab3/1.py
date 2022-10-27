''' Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby'''

a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))

if a>b:
    a,b = b,a   #zamieniamy miejscami

while a<=b:
    print(a, end=" ")   #end ze wartosci wyswietlaja sie w 1 linii
    a+=1

'''
temp=x
x=y
y=temp '''