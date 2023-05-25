from time import sleep
print('Olá eu sou um simulador de viagens')
print('AGUARDE...')
sleep(2)
d = float(input('Quantos km´s tem até seu destino ?'))
d1 = d*0.50
d2 = d*0.45
if d <=200 :
    print('Sua viagem terá um custo de :{:.2f}R$'.format(d1))
else:
    print('Sua viagem será :{:.2f}R$'.format(d2))

