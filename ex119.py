from random import randint
from time import sleep


def sorteio (lista):
    print('Os cinco numeros sorteados para a lista são: ',end='')
    for c in range(0, 5):
        n = randint(1, 10)
        print(f'{n}', end=' ')
        lista.append(n)
        sleep(0.5)
    print('PRONTO')


def somapar (numeros):
    print('A soma dos numeros pares dessa lista é: ', end='')
    somapar = 0
    for n in numeros:
        if n % 2 == 0:
            somapar += n
    print(f'{somapar}')



numeros = []
sorteio(numeros)
somapar(numeros)
