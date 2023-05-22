
n = int(input('Digite um numero: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c),end=' ')
print('\n\033[m O número {} foi dividido {} vezes'.format(n,t))
if t == 2:
    print('E por isso o ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
