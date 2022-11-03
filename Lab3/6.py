'''Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
break.'''

'''n = int(input("Podaj liczbę studentów: "))
x=1
b=0 #suma pkt

while x<=n:
    a = int(input(f"podaj liczbę punktów {x} studenta: "))
    if a<0 or a>100:
        continue
    b += a
    x += 1

sr=b/n
print("średnia wynosi: ", sr)'''

n = int(input("Proszę podać liczbę studentów: "))
a = 1 #wyświetlanie od 1 studenta
c = 0 #podstawienie pod dodawanie punktów
while True:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    if b<0 or b>100:
        continue
    c += b #sumowanie punktów studentów
    a += 1 #przechodzenie do kolejnego studenta
    if a==n+1:
        break

y = c/n #obliczanie średniej
print("Średnia wszystkich studentów",y)