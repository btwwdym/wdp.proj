n = int(input('Ile jest studentów?:'))
suma = 0
st = 1
while st <= n:
    x = int(input(f'Wpisz ilość punktów studenta {st}:'))
    suma += x
    st += 1
oc = suma/n
print(f'średnia liczba punktów w grupie: {oc}')
