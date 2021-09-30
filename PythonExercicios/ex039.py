from datetime import date

ano = int(input('Digite o ano de nascimento do jovem: '))
idade = date.today().year - ano
print('Este jovem tem {} anos.'.format(idade))
if idade < 18:
    print('Faltam {} anos para que este jovem faça alistamento militar.'.format(18-idade))
    print('O jovem precisa de alistar em {}.'.format(ano+18))
elif idade == 18:
    print('Já está na hora deste jovem fazer o alistamento militar.')
else:
    print('O tempo de alistamento já passou.\nEste "jovem" deveria ter se alistado a {} anos.'.format(idade-18))
