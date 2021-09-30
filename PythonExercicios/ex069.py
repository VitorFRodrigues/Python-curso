print('{:=^40}'.format(' CADASTRO '))
maior18 = menor20 = homens = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    print('=' * 40)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor20 += 1
    escolha = str(input('Deseja continuar? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:=^40}'.format(' CADASTRO REALIZADO '))
print(f'a) Maiores de 18 anos: {maior18}\n'
      f'b) Número de Homens: {homens}\n'
      f'c) Mulheres com menos de 20 anos: {menor20}')
