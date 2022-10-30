print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
x = int(input('Wpisz numer operacji:'))
a = float(input('Podaj argument 1:'))
b = float(input('Podaj argument 2:'))
if
if x == 1:
    w = a + b
elif x == 2:
    w = a - b
elif x == 3:
    w = a*b
elif x == 4 :
    if b == 0:
        print('nie wolno')
        exit()
    w = a/b
elif x == 5:
    w = a**b
print(f'Wynik: {w}')

