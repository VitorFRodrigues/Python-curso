dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}'.format(60*dias+0.15*km))