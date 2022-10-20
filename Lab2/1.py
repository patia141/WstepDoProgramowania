wiek = int(input("podaj wiek: "))

if wiek < 4:
    print("bilet bezpłatny")
elif wiek <= 18:
    print("bilet 10 zł")
else:
    print("bilet 20 zł")

