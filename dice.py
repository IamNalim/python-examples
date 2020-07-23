from random import *

pocet = int(input('Pocet kostek: '))
suma = 0
for i in range(0, pocet):
    suma = suma + randint(1, 6)

print('Suma {0} kostek se rovna {1}'.format(pocet, suma))
