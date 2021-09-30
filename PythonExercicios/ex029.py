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

vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você receberá uma multa no valor de R${}.'.format(7*(vel-80)))
else:
    print('Tenha um bom dia! Dirija com segurança!')