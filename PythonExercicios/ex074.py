from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
valores = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram ', end='')
for n in valores:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}.')
print(f'O menor valor sorteado foi {min(valores)}.')

'''maior = menor = valores[0]
for c in range(0, len(valores)):
    if maior < valores[c]:
        maior = valores[c]
    if menor > valores[c]:
        menor = valores[c]

print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')'''