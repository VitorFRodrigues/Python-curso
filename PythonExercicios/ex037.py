num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha a base de conversão
1 - Binário
2 - Octal
3 - Hexadecimal''')
base = int(input('Base: '))

if base == 1:
    print('Conversão Binária\nBase 10: {}\nBase 2: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('Conversão Octal\nBase 10: {}\nBase 8: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('Conversão Hexadecimal\nBase 10: {}\nBase 16: {}'.format(num, hex(num)[2:]))
else:
    print('Você não escolheu a base correta!\nReinicie o programa e escolha novamente!')
