numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_sorteado != numero_escolhido:
    print('Você errou o número, tente novamente...')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Você acertou! Parabéns!')

# Exemplo 02: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)
    contador += 1