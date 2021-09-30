sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    print('O funcionário receberá um aumento de 10% resultando em R${:.2f}'.format(sal*1.1))
else:
    print('O funcionário receberá um aumento de 15% resultando em R${:.2f}'.format(sal*1.15))