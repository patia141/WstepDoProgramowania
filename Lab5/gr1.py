#gr 1
list=[]
for x in range(5):
    liczba=int(input("Podaj liczbe: "))
    if (liczba>20) and ((liczba % 2) == 1):
            list.append(liczba)
print(list)