print('{:=^40}'.format(' Progressão Aritmética '))
primeiro = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da progressão serão: ', end=' ')
for c in range(0, 10):
    print(primeiro+razao*c, end=' -> ')
print('ACABOU')