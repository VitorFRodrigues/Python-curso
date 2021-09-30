nome = str(input('Digite seu nome completo: ')).strip()
div_nome = nome.split()
print('Primeiro = {}\nÚltimo = {}'.format(div_nome[0], div_nome[len(div_nome)-1]))