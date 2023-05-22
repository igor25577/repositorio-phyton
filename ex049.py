n = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))
if n > n2:
    print('O PRIMEIRO número digitado é maior')
elif n2 > n:
    print('O SEGUNDO número digitado é maior')
else:
    print('Não existe valor maior, os dois são IGUAIS.')
