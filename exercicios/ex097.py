n = []
while True:
    n.append(int(input('Digite um numero : ')))
    while True:
        r = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
n.sort(reverse=True)
print('-=-' * 40)
print(f'foram digitados {len(n)} numeros')
print(f'A lista de valores digitado acima em ordem descrescente é {n}')
if 5 in n:
    print('Na lista TEM o numero 5')
else:
    print('Na lista NÃO TEM o numero 5')