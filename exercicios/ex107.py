pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} : {v}')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} : {v}')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} : {v}')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append((estado.copy()))
print(estado)
