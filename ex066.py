from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa:'.format(c)))
    id = atual - nasc
    if id >= 18:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas da lista {} são maiores de idade e {} são menores'.format(maior, menor))
