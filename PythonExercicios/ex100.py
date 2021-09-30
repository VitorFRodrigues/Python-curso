from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
        sleep(.5)
    print('PRONTO!')


def somaPar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia()
somaPar(numeros)
