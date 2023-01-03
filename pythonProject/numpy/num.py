import numpy as np
# tab_1 = np.array([1,2,3], dtype = 'int32')
# print(tab_1, tab_1.dtype, tab_1.ndim, tab_1.shape)
# tab_11 = tab_1.astype('float32')
# print(tab_11,tab_11.dtype)

# tab_2 = np.array([5, 6, 7, 8])
# print(f'tab_2 {tab_2}')
#
# tab_3 = np.array((9, 10, 11, 12))
# print(f'tab_3 {tab_3}', tab_3.dtype)
#
# tab_4 = np.array(range(-4, 5))
# print(f'tab_4 {tab_4}', tab_4.dtype)
#
# tab_5 = np.arange(5, 10, 0.5)
# print(f'tab_5 {tab_5}')
#
# tab_6 = np.random.randn(5)
# print(f'tab_6 {np.round(tab_6, 2)}')
#
# tab_7 = np.zeros(10)
# print(f'tab_7 {tab_7}', tab_7.dtype)
#
# tab_8 = np.ones(10)
# print(f'tab_8 {tab_8}')
#
# tab_9 = np.full(5, -1)
# print(f'tab_9 {tab_9}', tab_9.dtype)
#
# tab_10 = np.empty(4)
# print(f'tab_10 {np.round(tab_10, 2)}')
#
# tab_11 = np.linspace(start = 10, stop = 50, num = 5)
# print(np.round(tab_11, 2))


# tab_1 = np.arange(1,11)
# print(f'tab_1: {tab_1}')
# # Długość tablicy
# print(f'Długość: {tab_1.size}')
# # Proste działania arytmetyczne
# print(f'Dodawanie: {tab_1 + 2}')
# print(f'Odejmowanie: {tab_1 - 2}')
# print(f'Mnożenie: {tab_1 * 2}')
# print(f'Dzielenie: {tab_1 / 2}')
# print(f'Potęgowanie: {tab_1 ** 2}')
# print('--- Tab2 ---')

# tab_2 = np.arange(10, 101, 10)
# print(f'tab_2: {tab_2}')
# print(f'Dodawanie tablic: {tab_1 + tab_2}')
# print(f'Odejmowanie tablic: {tab_1 - tab_2}')
# print(f'Mnożenie tablic: {tab_1 * tab_2}')
# print(f'Dzielenie tablic: {tab_1 / tab_2}')
# print(f'Potęgowanie tablic: {tab_2 ** tab_1}')

# tab_3 = np.array([1, 2, 3, 4])
# tab_4 = np.array([1, 3, 3, 5])
# same = tab_3 == tab_4
# print(f'Porównanie: {same}')
# print(f"tab3[porownanie]: {tab_3[same]}")
#
# porownanie = tab_3 < tab_4
# print(f'Porównanie: {porownanie}')
# print(f"tab4[porownanie]: {tab_4[porownanie]}")

tab_2d = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])
print(tab_2d, tab_2d.shape, tab_2d.ndim)

tab2_2d = np.array(((0, 1), (3, 4), (6, 7)))
print(tab2_2d, tab2_2d.shape, tab2_2d.ndim)

D = {1:2, 3:4, 5:6}
tab3_2d = np.array(list(D.items()))
print(tab3_2d)

tab4_2d = np.random.randint(low=0, high =
11, size=(3,3))
print(tab4_2d, tab4_2d.shape, tab4_2d.ndim)







