from time import sleep


def maior (* num):
    mai = cont = 0
    print('Analisando numeros ...')
    sleep(2)
    for n in num:
        if n > mai:
            mai = n
        cont += 1
    if len(num) > 1:
        print(f'foram informados {cont} números Da lista {num} o maior numero é: {mai}')
    elif len(num) == 1:
        print(f'So foi digitado o numero {mai} portanto o maior numero é {mai}')
    else:
        print('Não foi digitado valor algum sendo assim não há valores maiores ou menores')
    print('-=-' * 30)


maior(7, 9, 5, 3, 1)
maior(5, 6, 4, 2)
maior(4, 1)
maior(6)
maior()
