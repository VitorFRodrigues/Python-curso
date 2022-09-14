# > VARIÁVEIS

# 1. Variáveis

idade = 26 # Criando uma variável

print(idade)

nome = 'Vitor Rodrigues'

print(nome)

"""
Tipos de variáveis

1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
3. str: cadeias de caracteres, ou seja, dados textuais (string)
4. bool: valores lógicos (booleanos): True ou False
"""

idade = 26
altura = 1.76
nome = 'Vitor Rodrigues'
estudando = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguadem de programação que você está estudando? ')

print(f'A linguagem que você está estudando é {linguagem}')
