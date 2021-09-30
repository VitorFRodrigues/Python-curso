lista = []
jogador = {}
gols = []
while True:
    print('-'*30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)
print(f'{"Cod":<3} {"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-'*40)
for c, valor in enumerate(lista):
    print(f'{c:>3} {valor["nome"]:<15}{str(valor["gols"]):<15}{valor["total"]:<15}')
print('-'*40)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if 0 <= resp <= (len(lista)-1) or resp == 999:
        if resp == 999:
            break
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[resp]["nome"]}:')
        for c, valor in enumerate(lista[resp]["gols"]):
            print(f'    No jogo {c+1} fez {valor} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {resp}! Tente novamente.')
    print('-' * 35)
print('<< VOLTE SEMPRE >>')
