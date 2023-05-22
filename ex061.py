n = int(input('Digite o numero que gostaria de saber a taboada:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))