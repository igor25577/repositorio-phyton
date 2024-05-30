cores = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'limpa':'\033[m',
         'cinza':'\033[37m'}
from time import sleep
c = str(input(' Qual tipo de combustivel seu carro utiliza?'))
p = float(input('Em sua cidade qual o preço do litro de {}{}{} ?'.format(cores['vermelho'],c,cores['limpa'])))
lpk = float(input('Quantos km´s seu carro faz com 1L de {}{}{} ?'.format(cores['vermelho'], c, cores['limpa'])))
d = float(input('Quantos km´s até seu destino ?'))
gg = d/lpk
t = gg*p
print('CALCULANDO')
sleep(2)
print('Em sua viagem de {}{:.2f}{} km´s seu carro vai gastar {}{:.2f}{} litros de {}{}{}'
      .format(cores['azul'], d, cores['limpa'], cores['cinza'], gg, cores['limpa'], cores['vermelho'],c,cores['limpa']))
print('Você ira gastar um total de {}{:.2f} R${} de combustivel'.format(cores['verde'],t,cores['limpa']))
