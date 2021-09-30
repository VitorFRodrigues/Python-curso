n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Sua média é {:.2f}.'.format(media))
if media < 5:
    print('Você foi REPROVADO!')
elif media >= 5 and media < 7:
    print('Você ficou de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')
