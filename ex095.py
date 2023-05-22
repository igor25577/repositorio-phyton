num = []
r = 'S'
while True:
    n = int(input('Digite um número : '))
    if n not in num:
        num.append(n)
        print('Número adiocionado com sucesso')
    else:
        print('Numero duplicado não adicionado a lista!')
    r = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('-=-' * 40)
num.sort()
print(f'Os numeros adicionados a lista foram: {num}')