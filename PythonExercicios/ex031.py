dist = float(input('Digite a diatância da viagem em Km: '))
if dist <= 200:
    print('O preço da passagem é {:.2f}.'.format(dist*0.50))
else:
    print('O preço da passagem é {:.2f}.'.format(dist*0.45))