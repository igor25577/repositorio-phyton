num = (int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite o ultimo numero: ')))
print(f'Você digitou os numeros {num} ')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro numero 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(f'Os numeros pares digitados são: {n}', end=' ')