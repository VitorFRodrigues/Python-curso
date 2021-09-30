'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

n = int(input('Digite um número: '))
fat = 1
print('{}! = '.format(n), end='')
while n != 1:
    fat *= n
    print('{}x'.format(n), end='')
    n -= 1
print('1 = {}'.format(fat))

'''n = int(input('Digite um número: '))
fat = 1
print('{}! = '.format(n), end='')
for c in range(n, 1, -1):
    print('{}x'.format(c), end='')
    fat *= c
print('1 = {}'.format(fat))'''