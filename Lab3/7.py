'''Za pomocą pętli for wypisz na ekranie ciągi liczb:
• 1, 2, 3, ... , 99, 100
• 100, 99, ... , 2, 1, 0
• 7, 14, 21, ... , 70, 77
• 20, 18, ... , 2, 0'''

for i in range(1,101):
    print(i, end=' ')

for a in range(100,-1):
    print(a, end=' ')

for b in range(7,78,7):
    print(b, end=' ')

for c in range(20,-1,-2): #jeśli malejąco to krok też musi być malejący!!!
    print(c, end=' ')