import math
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_ad = float(input('Digite o comprimento do cateto adjacente: '))
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(cat_op, cat_ad, math.hypot(cat_ad, cat_op)))