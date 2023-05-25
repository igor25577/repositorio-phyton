cont = 1
while True:
    print('DIGITE NUMEROS NEGATIVOS PARA A PARADA')
    n = int(input('Digite o numero que deseja ver a tabuada: '))
    if n <= -1:
        break
    print(f'a taboada do número {n} é ...')
    while True:
        r = n * cont
        print(f'{n} X {cont} = {r}')
        cont += 1
        if cont >= 11:
            break
    cont = 1
print('FINALIZANDO O PROGRAMA ...')