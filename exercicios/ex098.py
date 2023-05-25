num = []
np = []
ni = []
while True:
    n = int(input('digite um numero : '))
    num.append(n)
    if n % 2 == 0:
        np.append(n)
    else:
        ni.append(n)
    while True:
        r = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
print(f'Os numeros digitados foram {num}')
print(f'Os numeros pares digitados foram {np}')
print(f'Os numeros impares digitados foram {ni}')
