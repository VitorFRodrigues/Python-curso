peso = float(input('Digite o peso da 1ª pessoa: '))
peso_maior = peso
peso_menor = peso_maior
for c in range(2, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso

print('O maior peso lido foi {}kg.\n'
      'O menor peso lido foi {}kg.'.format(peso_maior, peso_menor))