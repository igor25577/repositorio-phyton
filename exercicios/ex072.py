from time import sleep
azul = '\033[34m'
limpa = '\033[m'
print('§-' * 40)
print('{} MINHA RESOLUÇÃO {}'.format(azul, limpa))
print('§-' * 40)

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
o = int(input(''' O que deseja fazer:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
    SELECIONE UMA OPÇÃO:'''))
if o == 1:
    s = n1 +n2
    print('O numero {} se somado com {} dá um total de {}'.format(n1, n2, s) )
elif o == 2:
    m = n1 * n2
    print('Se pegarmos o numero {} e multiplicar por {} dá um resultado de {}'.format(n1, n2, m))
elif o == 3:
    maior = n1
    if n2 > n1:
        maior = n2
    print('Entre o numero {} e {} o maior é {}'.format(n1, n2, maior))
while o == 4:
    n3 = int(input('Digite o primeiro numero:'))
    n4 = int(input('Digite o segundo numero:'))
    o = int(input(''' O que deseja fazer:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
        SELECIONE UMA OPÇÃO:'''))
    if o == 1:
        s = n3 +n4
        print('O numero {} se somado com {} dá um total de {}'.format(n3, n4, s) )
    elif o == 2:
        m = n3 * n4
        print('Se pegarmos o numero {} e multiplicar por {} dá um resultado de {}'.format(n3, n4, m))
    elif o == 3:
        maior = n3
        if n4 > n3:
            maior = n4
        print('Entre o numero {} e {} o maior é {}'.format(n3, n4, maior))
while o != 5 and o != 4 and o != 3 and o != 2 and o != 1:
    print('OPÇÃO INVALIDA TENTE NOVAMENTE')
    for c in range(3,0,-1):
        sleep(1)
        print('Reiniciando em {} '.format(c))
    n1 = int(input('Digite o primeiro numero:'))
    n2 = int(input('Digite o segundo numero:'))
    o = int(input(''' O que deseja fazer:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
        SELECIONE UMA OPÇÃO:'''))
    if o == 1:
        s = n1 + n2
        print('O numero {} se somado com {} dá um total de {}'.format(n1, n2, s))
    elif o == 2:
        m = n1 * n2
        print('Se pegarmos o numero {} e multiplicar por {} dá um resultado de {}'.format(n1, n2, m))
    elif o == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre o numero {} e {} o maior é {}'.format(n1, n2, maior))
    while o == 4:
        n3 = int(input('Digite o primeiro numero:'))
        n4 = int(input('Digite o segundo numero:'))
        o = int(input(''' O que deseja fazer:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do programa
            SELECIONE UMA OPÇÃO:'''))
        if o == 1:
            s = n3 + n4
            print('O numero {} se somado com {} dá um total de {}'.format(n3, n4, s))
        elif o == 2:
            m = n3 * n4
            print('Se pegarmos o numero {} e multiplicar por {} dá um resultado de {}'.format(n3, n4, m))
        elif o == 3:
            maior = n3
            if n4 > n3:
                maior = n4
            print('Entre o numero {} e {} o maior é {}'.format(n3, n4, maior))
print('FINALIZANDO O PROGRAMA ...')
sleep(3)
print('FIM')
