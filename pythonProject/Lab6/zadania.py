'''                                            zadanie 1'''
'''def z1(imie= 'halo', wiek=20):
    print(imie, " ", wiek)
z1("heniek", 18)

z1("stefan", 33)

z1(wiek=15, imie="rich")'''

'''print(z1.__doc__)

print(help(z1))'''
'''                                            zadanie 2'''
'''def oblicz(liczba1, liczba2):
    a = liczba1 + liczba2
    b = liczba1 - liczba2
    return a, b

f = oblicz(2,3)
print(f[0], f[1])

a, b =oblicz(7.3,3.5)
print(a, b)'''
'''                                            zadanie 3'''
'''def func(*args):
    print(args)
    for i in args:
        print(i)

func(2,3,5,"hello")

func()

func("space", [4,5,6])'''

'''def maximum(*args):
    if len(args) == 0:
        return None
    m = args[0]
    for lb in args[1:]:
        if m < lb:
            m = lb
    return m

maks = maximum(1,5,7,10,-7)
print(maks)

maks = maximum()
print(maks)'''



'''def maximum1(a1, *args):
    m = a1
    for lb in args[1:]:
        if m < lb:
            m = lb
    return m

maks = maximum1(1,25,7,10,-7)
print(maks)

maks = maximum1(7)
print(maks)'''

'''                                                Zadanie 4'''
def fun(**kwargs):
    if 'end' in kwargs:
        temp = kwargs['end']
    else:
        temp = '\n'
    print(kwargs)
    for w in kwargs:
        print(w, ' = ', kwargs[w], end=temp)
fun(name="Kamil", wiek= 24, miasto="Kraków")
print()
fun(name="Kamil", wiek= 24, miasto="Kraków", end=' ')



