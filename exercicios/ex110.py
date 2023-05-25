from datetime import date
dados = {}
ano = date.today().year
dados['Nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Ano de nascimento: '))
dados['cart'] = int(input('Carteira de trabalho (tecle 0 caso não tenha):'))
idd = ano - dados["nasc"]
if dados['cart'] != 0:
    dados['contrac'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario R$: '))
print('-=-' * 20)
print(f'   -O nome cadastrado é:{dados["Nome"]}')
print(f'   -A pessoa cadastrada tem {idd} anos')
if dados['cart']:
    apos = dados['contrac'] + 35 + idd - ano
    print(f'   -O numero do seu CTPS É: {dados["cart"]}')
    print(f'   -O ano de contratação foi: {dados["contrac"]}')
    print(f'   -Recebe um salario de: R$ {dados["salario"]:.2f}')
    print(f'   -A pessoa cadastrada irá se aposentar com {apos} anos')
