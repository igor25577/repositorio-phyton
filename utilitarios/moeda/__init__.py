def metade(n = 0, formato=False):
    """

    :param n: valor monetario que deseja converter
    :param formato: se deseja formatar para moeda ou não True=sim padrão para não
    :return: retorna o valor formatado ou não dependendo do formato
    """
    res = n / 2
    return res if formato is False else moedas(res)


def dobro(n = 0, formato=False):
    res = n * 2
    return res if formato is False else moedas(res)


def aumento(n = 0, p = 0, formato=False):
    res = n + (n * p) / 100
    return res if formato is False else moedas(res)


def redutor(n = 0, p = 0, formato=False):
    res = n - (n * p) / 100
    return res if formato is False else moedas(res)


def moedas(n = 0, moeda = 'R$', formato=False):
    res = f'{moeda}{n:.2f}'.replace('.', ',')
    return res if formato is False else moedas(res)


def resumo(n = 0, p = 0, a = 0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'O PREÇO {moedas(n)} FOI ANALISADO')
    print('-=-' * 10)
    print(f'O dobro: \t{dobro(n,True)}')
    print(f'A metade: \t{metade(n,True)}')
    print(f'Aumentando {p}%: {aumento(n,p,True)}')
    print(f'Abaixando {a}%: {redutor(n,a,True)}')
    print('-=-' * 10)

8