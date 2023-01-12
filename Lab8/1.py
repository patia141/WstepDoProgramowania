'''Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
operatora in w celu sprawdzenia czy wartość występuje w liście.'''

import random
def find(list,x):
    list2=[]
    for i in range(len(list)):
        if list[i] == x:
            list2.append(i)
    return list2

lista=[random.randint(0,20) for a in range(10)]
print(lista)
b=int(input("podaj liczbe: "))
print(find(lista,b))