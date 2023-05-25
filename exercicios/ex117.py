from time import sleep


def contador(i, f, p):
    print(f'Contagem do numero {i} até o numero {f} de {p} em {p}')
    sleep(3)
    if p < 0:
        p *= - 1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM')
    print('-=-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez selecione: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
