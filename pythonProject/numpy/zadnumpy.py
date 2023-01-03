# Konwersja 8-bitowej liczby binarnej na liczbę dziesiętną.
# • Utwórz 8-elementową listę składaną o wartościach będących kolejnymi potęgami dwójki - [128 64 32
# 16 8 4 2 1]
# • Na podstawie tej listy utwórz tablice ndarray o nazwie wagi.
# • Utwórz drugą 8-elementową tablicę ndarray wypełnioną zerami i jedynkami (losowo) o nazwie
# liczba_bin.
# • Oblicz iloczyn tablic wagi i liczba_bin, a następnie policz sumę wartości iloczynu.

import numpy as np
import random
# lista_1 = [128, 64, 32, 16, 8, 4, 2, 1]
# wagi = np.array(lista_1)
# print(wagi)
# lista_2 = [random.randint(0,1) for x in range(len(lista_1))]
# liczba_bin = np.array(lista_2)
# print(liczba_bin)
#
# tab_1_2 = wagi * liczba_bin
# print(f'Liczba dziesiętna: {sum(tab_1_2)}')


# Utwórz losową macierz o wymiarach 5x5.
# Znajdź największy i najmniejszy element. (patrz tab4_2d;
# metoda max(), min())
# • Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
# • Policz sumę wartości w poszczególnych wierszach.

macierz = np.random.randint(low = 0, high = 70, size = (5,5))
print(macierz)

print(f'Max of matrix is: {macierz.max()}.', f'Min of matrix is: {macierz.min()}')
print('Max of axis 1: ', macierz.max(axis=1))
print('Max of axis 0: ', macierz.max(axis=0))
print('Suma wiersz: ', macierz.sum(axis=1))


