#Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.

litera = input("podaj literę:" )
if 'a' <= litera <= 'z' :
    print("litera jest mała")
elif 'A' <= litera <= 'Z':
    print("litera jest duża")
else :
    print("to nie jest litera")