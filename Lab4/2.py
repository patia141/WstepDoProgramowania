'''• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę'''

import random
zestaw_1=[]
x=1
ilosc1 = int(input("podaj liczbę elementów: "))
#for i in range(n):
while x<=ilosc1:
    zestaw_1.append(random.randint(1,10))
    x+=1
print(zestaw_1)

zestaw_2=[]
y=1
ilosc2 = int(input("podaj liczbę elementów: "))
while y<=ilosc2:
    zestaw_2.append(random.randint(5,15))
    y+=1
print(zestaw_2)

#3
a = int(input("podaj liczbę: "))
if a in zestaw_1:
    print("liczba z zestawu 1")
elif a in zestaw_2:
    print("liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

#4
zestaw_1_2 = zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)