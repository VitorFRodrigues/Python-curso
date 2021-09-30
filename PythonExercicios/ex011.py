comp = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².\nPara pintar esta parede, você precisará de {:.2f}l de tinta.'.format(comp, h, comp*h, comp*h/2))