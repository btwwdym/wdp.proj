a = int(input('Podaj liczbę 1:'))
b = int(input('Podaj liczbę 2:'))
if a > b:
    a, b = b, a
while a <= b:
    print(a, end=' ')
    a += 1