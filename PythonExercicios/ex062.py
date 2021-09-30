print('{:=^40}'.format(' Progressão Aritmética '))
primeiro = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da progressão serão: ', end=' ')

cont = 0
termos = 10
while cont != termos:
    proximo = primeiro+razao*cont
    print(proximo, end=' -> ')
    cont += 1
    if cont == termos:
        print('')
        aux = int(input('Você quer que mostre mais termos? Digite 0 se não quiser: '))
        termos += aux
print('ACABOU! A progressão foi finalizada com {} termos exibidos.'.format(termos))
