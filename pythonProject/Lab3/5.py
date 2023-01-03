def prog(l1, val):
    h = 0
    for a in range(len(l1)):
        if l1[a] == val:
            h = h + 1
    return h
lista = []
for i in 'programowanie':
    lista.append(i)
print(lista)
g = 'a'
f = prog(lista, g)
print(f'Liczba znaków: {f}')