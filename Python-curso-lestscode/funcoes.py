# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...

print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho desta lista
max() # - Retorna o maior valor de uma lista

# 2. Criação de Funções

# Função inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
# Função com parâmetros

def saudacao(nome, curso):
    print('Seja bem-vinda(o)!')
    print(f'Olá {nome}, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Vitor', 'python')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print('Seja bem-vinda(o)!')
    print(f'Olá {nome}, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Vitor')

# Função com retorno

def soma(num1, num2):
    soma = num1 + num2
    return soma

resultado = soma(7, 3)
print(f'A soma de 7 com 3 é {resultado}')

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1+num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1*num2
    elif operacao == '/':
        return num1/num2
    else:
        print('operador não implementado!')

resultado = calculadora(10, 20)
print(resultado)