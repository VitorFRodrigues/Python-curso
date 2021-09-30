pd = float(input('Digite o preço do produto: R$'))
desc = 5
print('Se você compra-lo a vista, terá {}% de desconto, cujo preço será de R${:.2f} reais.'.format(desc,pd*(100-desc)/100))
