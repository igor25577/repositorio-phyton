ne =('zero','um', 'dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('TENTE NOVAMENTE, Digite um numero de 0 a 20: '))
print(f'O numero que você escolheu quando lido de maneira extensa é : {ne[n]}')