nome = input('Digite seu nome completo: ').strip()

print('Nome maiúsculo: {}'.format(nome.upper()))
print('Nome minúsculo: {}'.format(nome.lower()))
#nome_div = nome.split()
#primeiro_nome = len(nome_div[0])

print('Número total de letras do seu nome: {}'.format(len(nome) - nome.count(' ')))
print('Número de letras do primeiro nome: {}'.format(nome.find(' ')))
