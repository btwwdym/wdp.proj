'''Zadanie 1. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
operatora in w celu sprawdzenia czy wartość występuje w liście.'''


'''import random
def find(lista, wartosc):
    lista2 = []
    for i in range(len(lista)):
        if lista[i]==wartosc:
            lista2.append(i)
    return lista2
lista = [random.randint(0,20) for x in range(10)]
print(lista)
userIn=int(input("Podaj szukaną wartość: "))
print(find(lista, userIn))'''

'''Zadanie 2. Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:'''

'''
dict1 = {'data1': 10, 'data2': -4, 'data3': 2}

def sum_of_values(dict1):
    s = 0
    for a in dict1.values():
        s = s + a
    return s
dict1 = {'data1': 10, 'data2': -4, 'data3': 2}
f = sum_of_values(dict1)
print(f)'''


'''Zadanie 3. Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.
'''


'''def potega(w, p):
    wynik = []
    if len(w) != len(p):
        print('Nie ta sama długość list')
        return wynik
    for b in range(len(w)):
        wyn = w[b] ** p[b]
        wynik.append(wyn)
    return wynik

lista1 = [2, 3, 4, 5, 6]
lista2 = [2, 3, 4, 5]

a = potega(lista1, lista2)
print(a)
'''

'''Zadanie 4.Napisz funkcję znaki(), która zlicza znaki w string’u za pomocą słownika: znaki stanowią klucze, liczba
znaków – wartości. Parametrem funkcji jest string. Funkcja ma zwracać słownik z wynikami. Wypisz słownik
uporządkowany według kluczy.
Wskazówka: użyj metody get(), która przy dostępie do wartości klucza, którego nie ma w słowniku,
zgłasza wyjątek KeyError. Aby uniknąć tego błędu metoda get może zwrócić wartość zdefiniowaną przez
użytkownika (drugi parametr).'''

def znaki(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    #     if char in result:
    #         result[char] = result[char] + 1
    #     else:
    #         result[char] = 1
    return result
s = 'znaki napisu'
ch = znaki(s)
print(ch)

for k in sorted(ch.keys()):
    print(k, ch[k])




