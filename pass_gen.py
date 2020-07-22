# Generator of random pass

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = '0123456789'
symbols = '[]{}();/,._-'

together = lower + upper + numbers + symbols
length = 16

ano = 'ano'

while ano == 'ano':
    password = ''.join(random.sample(together, length))
    print('Vase heslo: ' + password)
    print('Chcete vygenerovat dalsi? [ano/ne]: ')
    ano = input()
    ano = ano.lower()

print('Dekuji za pouzivani generatoru hesel')
