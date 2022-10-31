n = int(input('Ile jest studentów?:'))
suma = 0
st = 1
while True:
    if st > n:
        break
    x = int(input(f'Wpisz ilość punktów studenta {st}:'))
    suma += x
    st += 1
    if 0 < x < 100:
        continue
    else:
        print('Liczba niepoprawna')
        exit()
oc = suma/n
print(f'średnia liczba punktów w grupie: {oc}')
