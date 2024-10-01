print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Digite quantos termos você deseja ver: '))
t1 = 0
t2 = 1
cont = 2
numeros = [0,1]
print('~' * 30)
print('{} --> {} --> '.format(t1, t2), end='')
while cont < n:
    t3 = t1 + t2
    print('{} --> '.format(t3), end ='')
    t1 = t2
    t2 = t3
    cont += 1
    numeros.append(t3)

if n == 0 or n == 1:
        print('\n O numero {} faz parte da sequencia de Fibonacci.'.format(n))
elif n in numeros:
        print('\n O número {} faz parte da sequência de Fibonacci.'.format(n))
else:
        print('\n O número digitado  não faz parte da sequência de Fibonacci.')





print('FIM')
