from datetime import date
ano_hoje = date.today().year
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = ano_hoje - ano_nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação'] - ano_nasc) + 35
print('-='*30)
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v}')
