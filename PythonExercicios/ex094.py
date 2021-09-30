lista = []
cadastro = {}
qtd = tot_idade = 0
lista_mulheres = []
cadastro_mulheres = {}
lista_velhos = []
cadastro_velhos = {}
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
    tot_idade += cadastro['idade']
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
media = tot_idade/len(lista)
for c, valor in enumerate(lista):
    for k, v in valor.items():
        if k == 'sexo' and v == 'F':
            cadastro_mulheres['nome'] = lista[c]['nome']
            cadastro_mulheres['sexo'] = lista[c]['sexo']
            cadastro_mulheres['idade'] = lista[c]['idade']
            lista_mulheres.append(cadastro_mulheres.copy())
        if k == 'idade' and v > media:
            cadastro_velhos['nome'] = lista[c]['nome']
            cadastro_velhos['sexo'] = lista[c]['sexo']
            cadastro_velhos['idade'] = lista[c]['idade']
            lista_velhos.append(cadastro_velhos.copy())
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.\n'
      f'- A média de idade é de {media:.2f} anos.\n'
      f'- As mulheres cadastradas foram: ', end='')
for c in lista_mulheres:
    print(f'{c["nome"]}; ', end='')
print(f'\n- Lista das pessoas têm idade acima da média: ')
for c in lista_velhos:
    for k, v in c.items():
        print(f'    {k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
