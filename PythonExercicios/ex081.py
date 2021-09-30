lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
print('-='*40)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista de Valores decrescente: {lista}.')
if 5 in lista:
    print('O valor 5 encontra-se na lista.')
else:
    print('O valor 5 não encontra-se na lista.')
