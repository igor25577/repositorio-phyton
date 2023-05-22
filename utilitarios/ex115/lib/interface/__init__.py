from utilitarios.estruturas import *
from utilitarios.dados import *
from utilitarios.ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    sleep(1)
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        entrada('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        entrada('Saindo do programa ... Até mais')
        break
    else:
        print('\033[1;31mERRO, Digite uma opção válida\033[m')
