wiek = int(input('wprowadź wiek:'))
if wiek <= 0:
    print('wiek nie poprawny')
    exit()
else:
 if 0 < wiek <= 4:
    y = 0
 elif 4 < wiek <= 18:
    y = 10
 elif wiek > 18:
    y = 20
print('Cena biletu {} zł.'.format(y))

#def zbad(liczba):
 #   if liczba & 1 == 0:
 #       return 'liczba {} parzysta'.format(liczba)
#    return 'liczba {} nieparzysta'.format(liczba)
#for x in range(1,11):
 #   print(zbad(x))

