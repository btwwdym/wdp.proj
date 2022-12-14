'''                                                zadanie 2'''
'''zestaw_1 = []
zestaw_2 = []
licz1 = int(input('Liczba elementów:'))
import random
for b in range(licz1):
    l1 = random.randint(1,10)
    zestaw_1.append(l1)
print(zestaw_1)
licz2 = int(input('Liczba elementów:'))
for c in range(licz2):
    l2 = random.randint(5,15)
    zestaw_2.append(l2)
print(zestaw_2)
abc = int(input('Podaj liczbę:'))
if abc not in zestaw_1 and zestaw_2:
    print('Nie ma takiej liczby w obu zestawach')
else:
    if abc in zestaw_1:
        print('Liczba z zestawu 1')
    elif abc in zestaw_2:
        print('Liczba z zestawu 2')
zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)'''
'''                                                        zadanie 3'''
'''animals = []
an = int(input('Podaj liczbę zwierząt:'))
for f in range(an):
    x = input('Podaj zwierzę:')
    animals.append(x)
print(animals)
print(animals[0], animals[-3:], len(animals))
animals.sort()
print(animals)'''
'''                                                            zadanie 4'''
'''Utwórz listę imiona zawierającą dziesięć imion ('Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr',
'Zuzia', 'Bartek', 'Jacek'). Następnie
• Zmień imię znajdujące się na czwartej pozycji
• Wstaw dowolne imię jako piąty element
• Usuń siódmy element z listy
• Wyświetl listę imion po zmianach
• Dodaj do listy trzy ulubione imienia na trzech pierwszych pozycjach
• Usuń z listy imię podane przez użytkownika
• Zmień ostatnie imię na liście
• Wyświetl trzy pierwsze oraz trzy ostatnie imienia na liście
• Pobierz imię od użytkownika. Wyświetl informację, czy podane imię znajduje się na Twojej liście.
• Wyświetl posortowaną listę
• Wyświetl imiona w kolejności od Z do A
• Wyczyść drugą połowę listy, następnie wyświetl liczbę elementów listy.'''

'''imiona = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr','Zuzia', 'Bartek', 'Jacek']
imiona[3] = 'Janusz'
imiona.append('Kamil')
imiona.pop(6)
print(imiona)
imiona = ['Natalia', 'Billy', 'Damian'] + imiona
im = input('Podaj imię:')
imiona.remove(im)
imiona[-1] = 'Konrad'
print(imiona)
print(imiona[:3] + imiona[-3:])
imie = input('Imie:')
if imie in imiona:
    print('Jest w liście')
else:
    print('Nia ma w liście')
imiona.sort()
print(imiona)
imiona.reverse()
print(imiona)
sr = len(imiona)//2
del imiona[sr:]
print(imiona, len(imiona))'''

'''                                                    ZADANIE 5'''
import random as rd
n = 15
punkty = []
for pkt in range(n):
    punkty.append(rd.randint(0,51))
print(punkty)

a = min(punkty)
b = max(punkty)
print(f'Max liczbą jest:{b}', f'Min liczbą jest: {a}')

licz = int(input('Podaj liczbę:'))
if licz in punkty:
    print('Indexem jest:',punkty.index(licz))
else:
    print('Error. Liczba nie występuje w liście')

sr = sum(punkty)/n
print(sr)


bg = 0
powyzej = []
ponizej = []
for c in range(len(punkty)):
    if punkty[bg] > sr:
        powyzej.append(punkty[bg])
    else:
        ponizej.append(punkty[bg])
    bg += 1
print(powyzej, ponizej)

