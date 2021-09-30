# Ordem de preferência aritmética:
# 1 - ()
# 2 - ** (Potência)
# 3 - *, /, //, % (Multiplicação, Divisão, Divisão Inteira, Módulo da divisão)
# 4 - +, - (Soma e subtração)

# Escrever nome em quantidade fixa de caracteres
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinhado a direita
print('Prazer em te conhecer {:^20}!'.format(nome)) # centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) # centralizado completado dom sinal =

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {} e \na divisão é {:.3f}'.format(s,m,d), end=' ')
print('\nDivisão inteira {} e \npotência {}'.format(di, e))
