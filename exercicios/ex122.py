def fatorial(n, show=False):
    """
    -> calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('X', end=' ')
            else:
                print(f'= {f}')
        else:
            print(f'O fatoria de {n} é {f}')


help(fatorial)
