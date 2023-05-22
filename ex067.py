maior = 0
menor = 0
for c in range(1,6):
    p = float(input('Quantos quilos pesa a {}ª pessoa ?'.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso é {} kg´s'.format(maior))
print('O menor peso é {} kg´s'.format(menor))
