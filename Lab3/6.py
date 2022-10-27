'''Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
break.'''

n = int(input("Podaj liczbę studentów: "))
x=1
b=0

while x<=n:
    a = int(input(f"podaj liczbę punktów {x} studenta: "))
    if 0 <= a <= 100:
        b += a
        x += 1
    else:
        x+=n
        continue

sr=b/n
print("średnia wynosi: ", sr)