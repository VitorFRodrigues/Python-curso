s = 0
mulheres = 0
nome_h = ''
idade_h = 0
for c in range(1, 5):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: '.format(c))).strip()
    idade = int(input('Idade: '.format(c)))
    sexo = str(input('Sexo [M/F]: '.format(c))).strip().lower()
    s += idade
    if sexo == 'm' and idade > idade_h:
        idade_h = idade
        nome_h = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1

print('A média das idades do grupo é {:.2f}.\n'
      'O nome do Homem mais velho tem {} anos e se chama {}.\n'
      'Existem {} mulheres com menos de 20 anos no grupo.'.format(s/4, idade_h, nome_h, mulheres))
