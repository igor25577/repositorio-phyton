n = int(input('Digite um número para calcular seu fatorial :'))
c = n
f = 1
while c > 0:
    print(' {} '.format(c),end='')
    print(' X ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print('{}'.format(f))

print('+-' * 40)
print('OUTRA RESOLUÇÃO...')
print('+-' * 40)

n = int(input('Digite um número para calcular seu fatorial :'))
f = 1
for c in range (n, 0, -1):
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
print('{}'.format(f))
