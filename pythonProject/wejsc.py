lista = []
for i in range(5):
    licz = int(input('Podaj liczbę'))
    a = licz%2
    if a == 1:
        lista.append(licz)
    print(lista)
