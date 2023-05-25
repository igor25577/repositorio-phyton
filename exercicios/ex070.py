s = 0
while s != 'M' and s != 'F':
    s = str(input('Qual o seu sexo [M/F] ?')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('Tente novamente!')
print('Sexo {} registrado com sucesso'.format(s))
print('FIM')