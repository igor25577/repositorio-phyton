print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Digite quantos termos você deseja ver: '))
t1 = 0
t2 = 1
cont = 2
print('~' * 30)
print('{} --> {} --> '.format(t1, t2), end='')
while cont < n:
    t3 = t1 + t2
    print('{} --> '.format(t3), end ='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
