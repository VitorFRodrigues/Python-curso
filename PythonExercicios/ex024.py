nome = input('Digite o nome de uma cidade: ').strip()
nome = nome.title()
print('Esta cidade começa com a palavra Santo?')
print('Santo' in nome[:5])
