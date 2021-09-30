lista = []
dado = []
while True:
    lista.append(str(input('Nome: ')).strip())
    for c in range(1, 3):
        dado.append(float(input(f'Nota {c}: ')))
    media = (dado[0] + dado[1])/2
    dado.append(media)
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
no = 0
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{no:<4}{lista[c]:<10}', end='')
        no += 1
    if c % 2 == 1:
        print(f'{lista[c][2]:>8.2f}')
print('-'*25)
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        break
    print(f'As notas de {lista[2*resp]} são {lista[2*resp+1][0:2]}.')
    print('-' * 25)
print('FINALIZANDO...\n'
      '<<< VOLTE SEMPRE >>>')
