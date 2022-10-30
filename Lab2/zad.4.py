x = input('litera:')
if len(x) > 1 and len(x) == 0:
    print('niepoprawne dane')
    exit()
if x >= 'a' and x <= 'z':
    print('mala litera')
elif 'A' <= x <= 'Z':
    print('duża')
else:
    print('pozostałe')

# ord('z') zwraca kod ascii
# chr(kod) zwraca znak