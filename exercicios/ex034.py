print('Aqui verificaremos se seu carro ainda irá pagar ipva')
tempo = int(input('quantos anos tem seu carro?'))
if tempo<=20:
    print('paga ipva')
else:
    print('Não paga ipva')
print('--FIM--')

print('ou')

tempo = int(input('quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('--FIM--')
