def fatorail(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a : {fatorail(n)}')

f1 = fatorail(5)
f2 = fatorail(4)
f3 = fatorail()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('É impar!')
