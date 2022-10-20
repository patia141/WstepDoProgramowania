#zad3
print(''' Jaką operację chcesz wykonać?
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie
5 - potęgowanie
6 - wyjście ''')
operacja = int(input("wybierz operację: "))
a = int(input("podaj 1 liczbę: "))
b = int(input("podaj 2 liczbę: "))
wynik = 0

#while operacja != 6:
if operacja == 1:
    wynik = a + b
elif operacja == 2:
    wynik = a - b
elif operacja == 3:
    wynik = a * b
elif operacja == 4:
    if b==0:
        print("nie dziel przez 0")
        exit()
    wynik = a / b
elif operacja == 5:
    wynik = a ** b
else:
    print("niepoprawna operacja")
    exit()

print(wynik)