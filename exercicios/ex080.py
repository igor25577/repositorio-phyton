n = cont = s = 0
while True:
    print('Digite 999 caso queira parar')
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} numeros e somando eles tem um resultado de {s}')
