a = int(input('Podaj liczbę 1:'))
b = int(input('Podaj liczbę 2:'))
if a == b:
    print('Liczby są równe')
    exit()
else:
    if a < b:
       while a <= b:
           print(a)
           a += 1
    elif b < a:
        print(b)
        b += 1
print('Koniec')



