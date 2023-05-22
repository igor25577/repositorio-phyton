num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop()
print(num)
del num[0]
print(num)
num.remove(2)
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não existe o numero 5 na lista')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim')