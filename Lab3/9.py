'''Napisz program, który wyświetli „choinkę” jak poniżej. Wysokość „choinki” powinna być
podawana z klawiatury.
Wersja łatwiejsza (trójkąt):
4
*
* *
* * *
* * * *
Wersja trudniejsza:
4
   *
  * *
 * * *
* * * *'''

x = int(input("podaj liczbę: "))
for i in range(1,x+1):
    print(end=' ' * (x-i))
    print("* " * i)