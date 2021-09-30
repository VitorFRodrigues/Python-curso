num = int(input('Digite um número: '))
soma = maior = menor = num
escolha = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
cont = 1

while escolha == 's':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    escolha = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]

if cont > 1:
    print('Foram digitados {} valores.\n'
          'Media dos valores: {:.2f}\n'
          'Maior número: {}\n'
          'Menor número: {}'.format(cont, soma/cont, maior, menor))
else:
    print('Como só foi digitado apenas um único valor,'
          ' a média, maior e menor serão iguais a {}.'.format(num))
