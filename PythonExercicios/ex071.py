notas = [50, 20, 10, 1]
print('{:=^40}'.format(' CAIXA ELETRÔNICO '))
print(f'Cédulas disponíveis: R${notas[0]}.00, R${notas[1]}.00, R${notas[2]}.00 e R${notas[3]}.00')
cedulas = [0, 0, 0, 0]
valor = int(input('Digite o valor a ser sacado: R$'))
print('='*40)
for c in range(0, len(notas)):
    if valor // notas[c] > 0:
        cedulas[c] = valor // notas[c]
        valor -= cedulas[c]*notas[c]
    if cedulas[c] > 0:
        print(f'Todal de {cedulas[c]} cédulas de R${notas[c]:.2f}.')
print('='*40)
print('Volte Sempre!')
