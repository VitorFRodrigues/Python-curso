lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*40)
print(f'Você digitou os valores {lista}')
pos_max = []
pos_min = []
for c, v in enumerate(lista):
    if v == max(lista):
        pos_max.append(c)
    elif v == min(lista):
        pos_min.append(c)
print(f'O maior valor digitado foi {max(lista)}, nas posições ', end='')
for c in pos_max:
    print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)}, nas posições ', end='')
for c in pos_min:
    print(f'{c}... ', end='')
print()
