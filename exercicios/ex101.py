temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome :')))
    temp.append(float(input('Quantos kg/s você pesa ?')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar ? [S/N]')).strip()[0]
    if r in 'Nn':
        break
print(f'Ao todo foram cadastrados {len(princ)} pessoas')
print(f'O maior peso foi {mai:.2f}Kg´s peso do(a) ', end='')
for p in princ:
    if mai == p[1]:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {men:.2f}Kg´s peso do(a) ', end='')
for p in princ:
    if men == p[1]:
        print(f'[{p[0]}]', end=' ')
