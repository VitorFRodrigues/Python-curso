print('IMC - INDICE DE MASSA CORPÓREA')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

IMC = peso/(altura**2)
print('Seu IMC é {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif 18.5 <= IMC < 25:
    print('Você está no seu peso ideal.')
elif 25 <= IMC < 30:
    print('Você está com Sobrepeso.')
elif 30 <= IMC < 40:
    print('Você está Obeso.')
else:
    print('Você está com Obesidade Mórbida.')
