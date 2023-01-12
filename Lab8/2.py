'''Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
dict1 = {'data1':10, 'data2':-4, 'data3':2}
Nie wolno korzystać z funkcji sum().'''

def sum_of_values(dict):
    suma=0
    for x in dict.values():
        suma += x
    return suma

dict1 = {'data1': 10, 'data2': -4, 'data3': 2}
print(sum_of_values(dict1))