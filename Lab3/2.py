'''Napisz program, który wyświetli wartości funkcji 𝑦 = 2𝑥 2 − 5𝑥 − 8, dla 𝑥 ∈ [−4, 4],
z krokiem 0.5.'''

x = -4
while x <= 4:
    '''if -2 <= x <= 2:
            x=x+0.5
            continue - wracamy do if'''
    y = (2 * (x ** 2)) - (5 * x) - 8
    print(f"f({x})={y}")
    '''if x== -2:  /exit() - całkowicie wychodzimy z programu
        break       - wychodzimy z pętli'''
    x+=0.5

#print("koniec")