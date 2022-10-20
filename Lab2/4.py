'''zad4 Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości)i wypisuje ją
 na ekranie.'''

# ord(znak) - zwraca kod ASCII
# chr(kod) - zwraca znak

roznica = ord('a') - ord('A') #różnica pomiedzy dużą a małą literą

litera = input("podaj literę:" )
if 'a' <= litera <= 'z' :
    print(chr(ord(litera) - roznica))
elif 'A' <= litera <= 'Z':
    nowa=ord(litera)+roznica
    znak=chr(nowa)
    print(znak)
else :
    print("to nie jest litera")