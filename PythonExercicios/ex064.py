cont = soma = 0
num = int(input('Digite números aleatórios\n'
                'Digite 999 para parar: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite números aleatórios\n'
                    'Digite 999 para parar: '))
print('Foram digitados {} números, cuja soma é {}.'.format(cont, soma))