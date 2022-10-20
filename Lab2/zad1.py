a = int(input('Wprowadź wiek klienta:'))
if 0 < a <= 4:
    y = 0
elif 4 < a <= 18:
    y = 10
else:
    y = 20
print(f'Cena biletu {y} zl ')
