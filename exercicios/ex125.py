def notas (*notas, sit=False):
    """
    ->Função de analisar notas e situações de varios alunos
    :param notas: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma
    """
    tot = maior = menor = cont = 0
    situ = ''
    dados['total de notas'] = len(notas)
    for n in notas:
        tot += n
        cont += 1
        if n > maior:
            maior = n
            dados['maior nota'] = maior
        else:
            menor = n
            dados['menor nota'] = menor
    dados['media'] = tot / cont
    if sit:
        if dados['media'] < 5:
            dados['situação'] ='Ruim'
        elif dados['media'] > 5 < 7:
            dados['situação'] ='Razóavel'
        else:
            dados['situação'] ='Boa'


dados = {}
notas(7, 5, 4, 1, 9, sit=True)
print(dados)
