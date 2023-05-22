from utilitarios import dados
from time import sleep


def entrada(msg):
    print(linha())
    print(f'{msg}'.center(40))
    print(linha())


def linha(tam=42):
    return '-' * tam


def menu(lista):
    entrada('MENU PRINCIPAL')
    c = 1
    for p in lista:
        print(f'\033[1;33m{c} - \033[1;34m{p}\033[m')
        c += 1
    print(linha())
    op = dados.LeiaInt('\033[1;33mSua Opção: \033[m')
    return op

