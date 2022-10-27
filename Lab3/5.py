'''Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
wykorzystaniem pętli while'''

n = int(input("Podaj liczbę studentów: "))
x=1
b=0

while x<=n:
    a = int(input(f"podaj liczbę punktów {x} studenta: "))
    b += a
    x+=1

sr=b/n
print("średnia wynosi: ", sr)