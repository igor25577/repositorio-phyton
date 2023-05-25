from random import randint
win = 0
while True:
    print('-=-' * 40)
    nc = randint(0,11)
    np = int(input('Diga um valor:'))
    while True:
        escolha = str(input('Par ou impar? [P/I]')).strip().upper()[0]
        if escolha == 'P' or escolha == 'I':
            break
    tot = nc + np
    result = tot % 2
    print('-=-' * 40)
    if result == 0:
        print(f'Você jogou {np} e o computador jogou {nc} o total é de {tot} DEU PAR')
    else:
        print(f'você jogou {np} e o computador jogou {nc} o total é de {tot} DEU IMPAR ')
    print('-=-' * 40)
    if escolha == 'P':
        if tot % 2 == 0:
            win += 1
            print('Você VENCEU')
        else :
            print('Você PERDEU')
            break
    elif escolha == 'I':
        if tot % 2 == 1:
            win += 1
            print('Você VENCEU')
        else:
            print('Você PERDEU')
            break
        print('---' * 40)
print(f'ANTES DE PERDER VOCÊ GANHOU {win} VEZES CONSECUTIVAS! FINALIZANDO PROGRAMA ...')
