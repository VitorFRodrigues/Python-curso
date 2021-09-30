print('A soma entre todos os números ímpares que '
      'são múltiplos de 3 no intervalo de 1 a 500')
aux = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        aux += 1
        s += c
print('Foram encontrados {} multiplos de 3, resultando numa soma de {}.'.format(aux, s))