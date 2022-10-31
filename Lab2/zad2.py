x = input('Litera:')
if len(x) > 1:
    print('wpisz tylko 1 literę')
    exit()
else:
 if 'A' <= x <= 'Z':
    print('Duża')
 elif 'a' <= x <= 'z':
    print('mała')