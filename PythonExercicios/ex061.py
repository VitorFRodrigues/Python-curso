print('{:=^40}'.format(' Progressão Aritmética '))
primeiro = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da progressão serão: ')

cont = 0
while cont < 10:
    print(primeiro+razao*cont, end=' -> ')
    cont += 1
print('ACABOU')
