cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza':'\033[37m',
         'pretoebranco':'\033[7;30m'}

num = int(input('{}Digite um número: {}'.format(cores['roxo'], cores['limpa'])))
mod = num % 2
if mod == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))