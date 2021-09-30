lista = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
maior = menor = lista[0][1]
pes_pesadas = []
pes_leves = []
for p in lista:
    if p[1] == maior:
        pes_pesadas.append(p[0])
    elif p[1] == menor:
        pes_leves.append(p[0])
print(f'O maior peso foi de {maior}kg. Peso de {pes_pesadas}.')
print(f'O menor peso foi de {menor}kg. Peso de {pes_leves}.')
