print('-=-'*20)
print('Aprovação de empréstimo bancário')
print('-=-'*20)
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
tempo = int(input('Em quantos anos será efetuado o pagamento? '))

prestacao = valor/(tempo*12)

if prestacao > salario*0.3:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, tempo, prestacao))
    print('Empréstimo NEGADO, o valor da prestação é 30% acima do seu salário, favor adicionar mais parcelas.')
else:
    print('Emprestimo CONCEDIDO!\nO emprestimo será pago em {} parcelas de R${:.2f} reais'.format(tempo*12, prestacao))