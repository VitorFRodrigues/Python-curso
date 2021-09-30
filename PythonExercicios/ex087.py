matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-='*30)
soma_par = soma_terc_col = maior_seg_linha = 0
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
        if j == 2:
            soma_terc_col += matriz[i][j]
        if i == 1 and j == 0:
            maior_seg_linha = matriz[i][j]
        elif i == 1 and matriz[i][j] > maior_seg_linha:
            maior_seg_linha = matriz[i][j]
        print(f'[{matriz[i][j]}:^5]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma_par}.\n'
      f'A soma dos valores da terceira coluna é {soma_terc_col}.\n'
      f'O maior valor da segunda linha é {maior_seg_linha}.')
