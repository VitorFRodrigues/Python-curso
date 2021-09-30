for c in range(1, 7):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)

for c in range(0, 7, 2):
    print(c)

inicio = 2
fim = 9
passo = 3

for c in range(inicio, fim+1, passo):
    print(c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #significa: s = s + n
print('O somatório de todos os valores foi {}.'.format(s))
