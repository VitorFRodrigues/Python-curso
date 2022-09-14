for variavel in range(10):
    print(variavel)

for variavel in range(1,6):
    print(variavel)

for variavel in range(1, 12, 3):
    print(variavel)

soma = 0
for i in range(3):
    nota = float(input(f'Informe sua nota {i}: '))
    soma += nota
media = soma/3
print(f'Sua média é {media:.2f}')