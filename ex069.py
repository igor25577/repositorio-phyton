n = 1
par = 0
impar = 0
while n !=0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Deseja continuar [S/N]')).upper()
print('FIM')