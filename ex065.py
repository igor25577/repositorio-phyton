frase = str(input('Digite uma frase:')).strip().upper()
sep = frase.split()
junto= ''.join(sep)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase {} inversa é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase É um palíndromo')
else:
    print('A frase NÃO É um palíndromo')