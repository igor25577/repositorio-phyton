n = int(input('Digite o primeiro numero da PA :'))
r = int(input('Digite a sua razão :'))
cont = 0
while cont < 10:
    print('{} -->'.format(n), end=' ')
    n += r
    cont += 1
print('FIM')