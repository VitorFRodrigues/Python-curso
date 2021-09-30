#TEORIA
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

#PRÁTICA
pessoas = {'nome': 'Gustavo',
           'sexo': 'M',
           'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 90
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')