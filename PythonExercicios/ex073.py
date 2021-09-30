tabela = ('Flamengo', 'Palmeiras', 'Santos', 'Internacional', 'Cotinthians', 'São Paulo', 'Bahia', 'Grêmio',
          'Atlético-MG', 'Botafogo', 'Atletico-PR', 'Vasco da Gama', 'Ceará SC', 'Fortaleza', 'Goiás',
          'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('=-'*40)
print(f'Lista do Brasileirão: {tabela}')
print('=-'*40)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print('=-'*40)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('=-'*40)
tabela_ordem = sorted(tabela)
print(f'Times do Brasileirão (em ordem): {tabela_ordem}')
print('=-'*40)
colocacao = tabela.index('Chapecoense') + 1
print(f'Colocação da Chapecoense: {colocacao}ª posição.')
