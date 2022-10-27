print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')
op = int(input('Wpisz numer operacji:'))
a = float(input('Argument a:'))
b = float(input('Argument b:'))
if op == 1:
    wyn = a + b
elif op == 2:
    wyn = a - b
elif op == 3:
    wyn = a * b
elif op == 4:
    if b == 0:
        print('nie wolno')
        exit()
    else:
     wyn = a/b
elif op == 5:
    wyn = a ** b
print(f'Wynik {wyn}')
