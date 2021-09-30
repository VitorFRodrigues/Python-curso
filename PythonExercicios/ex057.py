sexo = 'A'
while sexo not in 'MF':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('Valor incorreto, digite novamente.')

print('Sexo {} digitado com sucesso.'.format(sexo))