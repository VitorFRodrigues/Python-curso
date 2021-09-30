lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    elif c % 2 == 1:
        lista_impar.append(c)
print('-='*30)
print(f'Lista: {lista}\n'
      f'Lista Pares: {lista_par}\n'
      f'Lista Impares: {lista_impar}')