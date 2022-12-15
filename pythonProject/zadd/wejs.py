# Grupa 1. Użytkownik podaje dwie liczby zmiennoprzecinkowe. Wypisz na ekranie większą z nich.

'''a = float(input('Liczba 1:'))
b = float(input('Liczba 2:'))
if a > b: print(a)
elif b > a: print(b)
else: print('Liczby są równe')'''

# Grupa 2. Użytkownik podaje dwie liczby całkowite. Sprawdź czy te liczby są różne.

'''a = int(input('Liczba 1:'))
b = int(input('Liczba 2:'))
if a != b:
    print('Liczby są różne')
else:
    print('Liczby są równe')'''

# Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
# mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.

'''a = int(input('Liczba 1:'))
b = int(input('Liczba 2:'))
if a > b:
    for c in range(b, a+1):
        print(c, end=" ")
elif b > a:
    for c in range(a, b+1):
        print(c, end=" ")
else:
    print('Liczby są równe')'''

#  Napisz program, który wyświetli wartości funkcji 𝑦 = 2𝑥^2 − 5𝑥 − 8, dla 𝑥 ∈ [−4, 4], z krokiem 0.5.

'''x = -4
while x < 4:
    a = 2*x ** 2 - 5*x - 8
    print(a, end=" ")
    x += 0.5'''

# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
# ujemnej, następuję wyjście z pętli.

'''while True:
    a = int(input('Liczba:'))
    if a >= 0:
        if a%2 == 0:
            print(a)
            continue
    else:
        break'''

# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
# liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
# wykorzystaniem pętli while.

'''n = int(input('Liczba studentów:'))
x = 1
sum = 0
while x <= n:
    lp = int(input(f'Liczba punktów studenta {x}:'))
    sum = sum + lp
    x += 1
    if 0 <= lp <= 100:
        continue
    else:
        exit()

print('Srednia licz punkt: ', sum/n)'''

#  Za pomocą pętli for wypisz na ekranie ciągi liczb:
# • 1, 2, 3, ... , 99, 100
# • 100, 99, ... , 2, 1, 0
# • 7, 14, 21, ... , 70, 77
# • 20, 18, ... , 2, 0

'''for b in range(20, -1, -2):
    print(b)'''

# Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
# powinna być podawana przez użytkownika.
# Przykład: 3
# * * *
# * * *
# * * *

'''a = int(input('liczba:'))
f = 1
for i in range(a):
    i = '*'
    print(i*f)
    f += 1'''

# Zadanie 1. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
# parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
# operatora in w celu sprawdzenia czy wartość występuje w liście.

'''import random as rn
def find(lista, val):
    lista2 = []
    for a in range(len(lista)):
        if lista[a] == val:
            lista2.append(a)
    return lista2
li = [rn.randint(0, 20) for x in range(10)]
print(li)
b = int(input('Liczba:'))
f = find(li, b)
print(f)'''


# Zadanie 2. Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
# dict1 = {'data1':10, 'data2':-4, 'data3':2}
# Nie wolno korzystać z funkcji sum().

'''def sum_of_values(slow):
    suma = 0
    for i in slow.values():
        suma = suma + i
    return suma



dict1 = {'data1':10, 'data2':-4, 'data3':2}

a = sum_of_values(dict1)
print(a)'''

# Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
# czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.

'''lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
def potega(lv, lp):
    lwyn = []
    if len(lv) != len(lp):
       exit()
    else:
        for i in range(len(lv)):
            wyn = lv[i] ** lp[i]
            lwyn.append(wyn)
    return lwyn

f = potega(lista1, lista2)
print(f)'''


