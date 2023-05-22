soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um numero inteiro:'))
    cont += 1
    if n % 2 == 0:
        soma += n
print('Você digitou {} numeros e a soma dos numeros pares que você digitou foi {}'.format(cont, soma))