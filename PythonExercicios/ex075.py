valores = (int(input('Digite o valor 1: ')),
           int(input('Digite o valor 2: ')),
           int(input('Digite o valor 3: ')),
           int(input('Digite o valor 4: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
