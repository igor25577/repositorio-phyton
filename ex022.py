tempo=int(input('quantos dias alugados?'))
distância=float(input('quantos km rodados?'))
t=(tempo * 60) + (distância * 0.15)
print('total a pagar:{:.2f} R$'.format(t))
