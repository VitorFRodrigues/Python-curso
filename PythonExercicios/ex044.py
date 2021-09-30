print('{:=^40}'.format(' ATACADÃO '))
valor = float(input('Qual o valor do produto? R$'))
print('''FORMAS DE PAGAMENTO:
1 - À Vista dinheiro/cheque
2 - À Vista no Cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
forma = int(input('Digite a forma de pagamento: '))

if forma == 1:
    print('O Valor do produto é R${:.2f}.'.format(valor*0.9))
elif forma == 2:
    print('O Valor do produto é R${:.2f}.'.format(valor*0.95))
elif forma == 3:
    print('O produto será pago em 2 parcelas de R${:.2f}.'.format(valor/2))
elif forma == 4:
    qtd = int(input('Digite quantas vezes você deseja parcelar: '))
    print('O produto será pago em {} parcelas de R${:.2f}, cujo valor total será R${:.2f}.'.format(qtd, valor*1.2/qtd, valor*1.2))
else:
    print('Forma de pagamento incorreta!')
