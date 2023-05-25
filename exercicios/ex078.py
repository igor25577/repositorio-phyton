r = 's'
cont = tot = media = 0
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar ? [S/N] ')).lower()
    cont += 1
    tot += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = tot / cont
print('''Você digitou {} e a media entre os numeros é {:.2f}
 o maior numero digitado foi: {} e o menor foi {} '''.format(cont, media, maior, menor))
print('FINALIZANDO O PROGRAMA ...')
