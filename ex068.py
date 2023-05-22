somaid = 0
idm = 0
maioridadeH = 0
nomevelho = 0
totM20 = 0
for p in range (1,5):
    print('-=-=-=-=-=-= {}ª PESSOA -=-=-==-=-=-'.format(p))
    n = str(input('Nome:'))
    id = int(input('Idade:'))
    sex = str(input('[M/F]: ')).upper()
    somaid += id
    if p == 1 and sex in 'Mm':
        maioridadeH = id
        nomevelho = n
    if sex in 'Mm' and id > maioridadeH:
        maioridadeH = id
        nomevelho = n
    if sex in 'Ff' and id < 20:
        totM20 += 1
idm = somaid / 4
print('A média de idade do grupo é {} anos'.format(idm))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeH, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totM20))