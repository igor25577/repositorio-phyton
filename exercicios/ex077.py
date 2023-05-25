n = int(input('Digite um numero :'))
tot = 0
cont = 0
while n != 999:
    print('Caso queira parar digite 999')
    tot += n
    cont += 1
    n = int(input('Digite um numero  :'))
print('Você digitou {} termos e soma de todos eles é {}'.format(cont, tot))
print('FINALIZANDO O PROGRAMA ...')
