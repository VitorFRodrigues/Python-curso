from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} dessas pessoas são maiores de idade e '
      '{} destas pessoas são menores de idade.'.format(maior, menor))
