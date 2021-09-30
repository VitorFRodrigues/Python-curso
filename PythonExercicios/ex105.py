def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    lista = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if lista['média'] >= 7:
            lista['situação'] = 'BOA'
        elif 5 <= lista['média'] < 7:
            lista['situação'] = 'RAZOÁVEL'
        else:
            lista['situação'] = 'RUIM'
    return lista


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
