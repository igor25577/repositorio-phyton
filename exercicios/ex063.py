print('=-' * 40)
print('Digite um numero para ver seus 10 primeiros termos de progressão aritmetica:')
print('=-' * 40)
n = int(input('digite um numero:'))
r = int(input('digite a razão da progressão:'))
décimo = n + (10 - 1) * r
for c in range(n, décimo + r, r):
   print('{}'.format(c), end=' -> ')
print('ACABOU')
