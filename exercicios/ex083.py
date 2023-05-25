sex = 0
c = 0
maior = menorf = h = 0
while True:
    id = int(input('Qual a sua idade ? '))
    while True:
        sex = str(input('Qual o seu sexo ? [M/F]')).strip().upper()[0]
        if sex == 'M' or sex == 'F':
            break
    while True:
        c = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
        if c == 'S' or c == 'N':
            break
    if id >= 18:
        maior += 1
    if sex == 'M':
        h += 1
    if id <= 19 and sex == 'F':
        menorf += 1
    if c == 'N':
        break
print(f'''Ao finalizar o programa foram cadatrados {maior} pessoas com mais de 18 anos e foram cadastrados {h} homens
e tambem {menorf} mulheres com menos de 20 anos''')
