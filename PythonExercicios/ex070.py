nome_barato = ''
barato = total = totmil = cont = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preco do produto: R$'))
    total += preco
    cont += 1
    if preco >= 1000:
        totmil += 1
    if cont == 1 or preco < barato:
        nome_barato = nome
        barato = preco
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:=^40}'.format(' COMPRA FINALIZADA '))
print(f'a) Total gasto na compra: R${total:.2f}\n'
      f'b) Número de produtos acima de R$1000.00: {totmil}\n'
      f'c) Produto mais barato: {nome_barato}\n'
      f'   Custo do produto mais barato: R${barato}')
