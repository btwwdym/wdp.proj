a = int(input('Podaj liczbę 1:'))
b = int(input('Podaj liczbę 2:'))
if a > b:
    a, b = b, a
while a <= b:
    if a % 2 == 1:
        a += 1
        continue
    print(a, end=' ')
    a += 1

