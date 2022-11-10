'''• Załóżmy, że lista X składa się z 10 elementów. Przenieś ostatnie trzy elementy z końca na początek
listy bez zmiany ich oryginalnej kolejności.
• Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y. Wyświetl obie listy
na ekranie.'''

X = list(range(10))
print(X)
X[:0]=X[-3:]
X[-3:]=[]
#del X[-3:]
print(X)

Y=X[:] #kopiowanie listy X
Y[4]=12
print(X)
print(Y)