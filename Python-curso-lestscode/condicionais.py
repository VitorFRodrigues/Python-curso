# > ESTRUTURAS CONDICIONAIS

idade = 20

if idade >=18:
    escolha = 'maior'
else:
    escolha = 'menor'

print(f'Você é {escolha} de idade')

"""
Imagine que você queira imprimir "Aprovada(o)", caso o estudante tenha uma média superior ou igual a 7 e "Reprovado", caso a média seja inferior a 7
"""

nota = float(input('Digite sua nota: '))

if nota >= 7:
    escolha = 'aprovado(a)'
elif nota >= 5:
    escolha = 'para recuperação'
else:
    escolha = 'reprovado(a)'

print(f'Você foi {escolha}!')

media = 10
presenca = 100

if media >=7 and presenca >= 70:
    print('Aprovado!')
    print('Parabéns!')
else:
    print('reprovado!')
    print('Tente novamente!')
