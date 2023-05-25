dados = {}
lista = []
media = somaid = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if dados['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F !')
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input('Idade: '))
    somaid += dados['idade']
    lista.append(dados.copy())
    while True:
        r = str(input('Deseja continuar ?[S/N]')).strip()[0]
        if r not in 'SsNn':
            print('ERRO! Responda apenas S ou N')
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
media = somaid / len(lista)
print('-=-' * 20)
print(f'A-) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B-) A media de idade é de {media:.2f} anos')
print(f'C-) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ',end='')
print(f'\nD-) lista das pessoas que estão acima da idade media: ', end='')
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}, ', end='')