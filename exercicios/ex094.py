num = []
mai = 0
men = 0
for c in range(0,5):
    num.append(int(input(f'DIgite um numero na {c}ª posição')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('-=-' * 40)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')
