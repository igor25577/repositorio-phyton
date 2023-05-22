print('ordem de precedência binaria:1º=(){}[].2º=**.3º=*,/,//,%.4º=+,-')
print('ex;5+3*2=11, 3*5+4**2=31, 3*(5+4)**2=243')

print(' para quebrar um linha usa;/n, e para imendar as linhas:end=')

print('os termos primitivos são:int,float,bool,str')

print('caso queira resumir um numero fracionado se utiliza a formula "(:.2f)')
print('ex;2.11558946 vai para;2.11')

print(' MANEIRAS CLASSICAS DE IMPOORTAÇÃO DE MODULOS')
print('quando quiser importar um modulo completo usa-se o comando;import+o que deseja importar')
print('Ex:import=bebida, vai importar a classe inteira de bebidas')
print('já quando quiser importar um modulo especifico utiliza-se from + a classe do que precisa importar + import + mais o item especifico')
print('ex:from+bebida+import+café, esse comanda vai importar somente o café da classe de bebidas')
print('um dos modulos que podemos importar é o:math')
print('as funcionalidades que vem no pack são:"ceil" para arredondar pra mais,"floor" para arredondar para menos,"trunc" que vai eliminar o numero dps da virgula,"pow" que vai potencializar o numero,"sqrt"que é para calcular a raiz quadrada,"factorial" para encontrar o fatorial de um numero')

print('para converter o seno e cosseno você usa o comando "radians" dps do comando de import')
print('ex:seno=math.sin(math.radians ângulo))')

print('MODULOS PARA MANIPULAÇÃO DE TEXTOS')
print('FATIAMENTO')
print(':usando esse modulo você pode retirar um caractere ou mais caracteres sem precisar escrever a frase inteira')
print('exemplo, frase =  digita algo, ao utilizar o modulo:frase[9] ele retira somente o caracter do micro espaço 9 que seria o caracter de 10º posição pois começa a contar do micro espaço 0')
print('para fatiamento usa-se tbm isso:frase=[9:13] ele seleciona os caracteres que estão nessas posições:9,10,11,12 porem exclue o 13 ,e sempre um a menos no final')
print('pode-se usar tambem:frase[9:21:2] dessa forma ele vai mostrar o caracter no micro-espaço 9 ate o caracter no micro espaço 20 porem pulando dois micro espaço por caracter mostrado, ex:9,11,13,15,17,19 ignorando os micro espaço 10,12,14,16,18,20')
print('da para usar tambem o: frase[:5] quando n coloca quando ele vai começar ele começa do micro espaço 0 que é o da 1º posição ate o caracter 4')
print('temos o: frase[15:] ele inicial a fatiar do micro-espaço 15 ate o ultimo caracter')
print('usa-se:frase[9::3] quando usa assim ele inicia do micro-espaço 9 e vai até o ultimo retirando um caracter e ignorando os 2 seguintes, ex:mostra o 9 depois mostra o 12 depois o 15 depois o 18')
print('ANALISE')
print('usando esse modulo você analisa a frase utilizando suas funções')
print('sua 1º função é:"len" então se eu utilizo o len ele vai me dar o cumprimento da frase ex:a frase tem 21 micro-espaço ')
print('a 2º função e o "count" utiliza-se ele da seguinte maneira:frase.count("caracter desejado") ao fazer isso ele vai contar quantas vezes aparece o caracter desejado')
print('obs: o count da para usar-se combinado com o fatiamento da seguinte maneira:frase.count("caracter desejado",0,13) ao fazer esse comando ele vai contar quantos caracteres desejado tem do micro-espaço 0 até o 12')
print('3º função :frase.find("deo") ele vai contar quantas vezes ele encontrou o deo na frase e em qual micro-espaço ele começou, ex:começa no 11 ')
print('uma extensão do find é o: frase.find("algo que não esteja na frase")ele vai te responder com um -1 que significa que n existe isso na frase ')
print('outra extensão é o: "palavra desejada" in frase, ao utilizar esse comando ele vai buscar se existe a palavra digitada dentro da frase mas sem identificar o micro-espaço que ela começa ou quantas vezes apenas vai dizer se sim ou não')
print('TRANSFORMAÇÃO')
print('esse modulo ele pode mudar a caracteristica de str que até então era inmudavel')
print('sua 1º função é: frase.replace("palavra que deseja mudar","palavra que deseja por no lugar") ao usar esse comando ele vai pegar a palavra antiga, ex:python e trocar pela nova, ex:android ou seja todas palavras python da frase vai virar android')
print('sua 2º função é:frase.upper() ao utilizar essa função transforma a frase toda em letras maiusculas, ex:oi gata, vai para OI GATA,')
print('sua 3º função é:frase.lower() ao utilizar essa função você transforma a frase inteira em letras minuscula, ex:OI GATA vai para oi gata')
print('sua 4º função é:frase.captalize() essa função transforma a frase inteira´em minuscula menos a primeira letra, ex:Oi Gata vai para Oi gata')
print('sua 5º função é:frase.title() essa função analisa quantas palavras sua frase tem e transforma em maiuscula a primeira letra de cada palavra ex: oi gata como està vai para Oi Gata Como Está')
print('sua 6º função é:frase.strip() essa função remove todos os espaços inuteis no inicio e no final exceto o meio da frase e a função pode ter a variante:"frase.rstrip() ao utilizar esse comando remove os espaços apenas do lado direito e "frase.lstrip" esse é para remover somente os espaços do lado esquerdo da frase')
print('DIVISÃO')
print('esse modulo servepara dividir frases')
print('sua 1º função é:frase.split() essa função divide espaços entre micro-espaços de maneira mais simples ele retira o caracter espaço e quebra a frase em diversas ordens de micro-espaços, ex:se antes a contagem de caracteres era 123456 e o 4 era um espaço, agora vai ser:123 12 definindo as palavras em numeros ex:palavra1, palavra,2 e etc')
print('para juntar a frase que o split dividiu usa-se o comando:"item que deseja usar na unificação ex:-".join(frase)')
print('DUVIDAS VÁ AO EX027')


print('CONDIÇÕES (SIMPLES)')
print('são comandos simples que fazem uma cadeia de rotas ex:carro vire a direita,carro siga em frenta,carro vire a esquerds , carro pare.')
print('e você pode representar mais de uma cadeia ex:se o carro for para esquerda esse sera o trajeto dele, ja se for para direita sera tal trajeto')
print('você pode utilizar opções de caminhos distintos usando os comandos, "if" e "else"')
print('ex:ifcarro.esquerda=esse dira o trajeto se ele for para esquerda e põe dentro eai coloca como bloco true, já se ele não for para esquerda utiliza o comando elsecarro.esquerda e o coloca como bloco false')
print('duvidas vá ao ex034')


print('COMO UTILIZAR CORES NO TERMINAL')
print('para utilizar o codigo ansi para cores usa-se:\033["codigo da cor desejada"m.... ex \033[0;33;44m')
print('EM CASO DE DUVIDAS VÁ AO EX045')


print('ESTRUTURAS ANINHADAS')
print('você pode aninhar comandos ex:ifcar.esquerda():, elif():, else(): sendo assim ele te da três ou mais opções de direção ao contrario da simples que são apenas duas caso queira usar mais de 3 funções é so usar mais de um "elif():"')
print('Em caso de duvidas vá ao ex 046')


print('ESTRUTURAS DE REPETIÇÃO')

print('LAÇOS EM INTERVALOS')
print('laços em intevalos é quantas vezes você irá repetir um comando de maneira automatica por exemplo eu tenho um comando para andar no jogo q seria  eu utilizo o laço da seguinte maneira "for c in rangek(1.10):" ele iria andar do bloco 1 ao 10')
print('laços tambem podem ser feitos com mais de uma ação por exemplo eu quero que o personagem de um ande e pule uma vez seguindo a ordem anda,pula,anda,pula ')
print('em laços tambem pode se usar a condição if para alguns detalhes que possa surgir no caminho')
print('EM CASO DE DUVIDAS VÁ AO ex057')

print('LAÇOS SEM INTERVALOS')
print('laços sem intervalos podem ser usados quando não se sabe a quantidade de repetição que precisa pra chegar ao objetivo então ela funciona com uma condição ex:enquanto meu personagem não chegar a maçã eu não paro de dar passos')
print('O comando utilizado pra isso é: whilenot():'
      '                                 passo')
print('DUVIDAS VÁ AO EX069')

print('LAÇOS COM PONTO DE PARADA')
print('laços com ponto de parada são laços que com um comando chamado (break) você pode sair do laço de repetição de maneira direta sem finalizar o comando ex (você tem toda um estrutura para buscar um item ou resposta mas se no meio do caminho achar algo mais interessante você pode utilizar um break para parar e sair do comando')
print('DUVIDAS VÁ AO EX 079')

print('VARIAVEIS COMPOSTAS (TUPLAS)')
print('com a variavel "tupla" você pode aumentar o espaço da variavel composta para mais de um espaço se antes o modulo so recebia um item agora ele pode guardar varios valores e você pode acessar os itens selecionando o indice do elemento ex 0,1,2,3... LEMBRE-SE AS TUPLAS SÃO IMUTÁVEIS')
print('DUVIDAS VÁ AO EX086')

print('VARIAVEIS COMPOSTAS (LISTAS)')
print('para utilizar a lista vc tem que usar colchetes e tambem ha um detalhe mt importante e que a lista podem ser modificadas')
print('para adicionar elementos nas listas utiliza se o comando .append(item)')
print('para apagar pode se usar os comandos (del, pop, e o remove) quando utiliza se o comando del vc precisa colocar a posição do elemento em colchetes ja no pop a posição deve ser entre parentes e o remove você precisa colocar o nome do elemento')
print('DUVIDAS VÁ AO EX:093')

print('VARIAVEIS COMPOSTA (LISTAS DENTRO DE LISTAS OU LISTAS COMPOSTAS)')
print('listas compostas são listas dentro de listas ou seja com uma unica lista você pode armazenar um banco de dados há duas maneiras de realiza-la, uma delas é criar duas variaveis ex lista A e lista B e então você faz da seguinte maneira listaB.append(listaA) e então todas informações da listaA vão parar em um unico espaço da listaB e tambem da para fazer com o comando mais simples ex: lista =[[informaçoes],[informações],[informações]]')
print('em listas compostas você tambem pode retirar um item especifico como exemplo:print(lista[0][1]) ele vai pegar o item da lista zero na posição 1')
print('DUVIDAS VÁ AO EX 100')

print('VARIAVEIS COMPOSTAS (DICIONARIOS)')
print('Os dicionarios em python podem ser identificados com dict() ou dados = {}')
print('nos dicionarios você pode nomear os dados ex dados = {nome:pedro,idade:25} fazendo isso você pode pegar as informações de maneira mais direta como por exemplo:print(dados[nome]) ele ja escrevera o nome colocado')
print('em dicionarios n se utiliza o append você ja cria de maneira direta ex dados[sexo]=m ja adiciona de maneira automatica')
print('para apagar elementos em dicionario utiliza-se o comando del')
print('No dicionario há comandos como values() com o values você pegara informações que estão dentro das chaves, ha outro comando que é o keys() pega informações nomeadas,e com o items você pega tanto as keys quanto os values')
print('Os dicionarios tambem podem ser combinados com listas')
print('DUVIDAS VA AO EX:107')

print('FUNÇÕES PARTE 1')
print('Fora as funções do python você tambem pode criar a sua propria função personalizada para o seu uso')
print('O comando para criar a sua rotina você utiliza o def"nomedocomando"(): e uma linha adentro e a função que deseja criar')
print('tambe dá para criar parametros que são meio que uma combinação de funções')
print('Ex: defmensagem(msg): coloca as funções linha adentro e digita msg onde deseja que passe a mensagem')
print('DUVIDAS VA AO EX 114')

print('FUNÇÕES PARTE 2')
print('O python tem uma função de ajuda interativa para utiliza-la basta usar o comando "help()" mas so da para utiliza-lo no console python')
print('Alem do help para acessar informações sobre as funções temos o comando "print(função desejada __doc__')
print('Há tambem as docs streangs basta colocar tres aspas duplas em baixo da def desejada os docs servem para fazer um guia de uma função para você mesmo ou ate mesmo algum usuario de python que acabe usando sua def')
print('Em funções tbm temos o parametro opcional que pode ser usado para deixar valido ou não uma opção para usalo basta você fazer um parametro receber o valor zero assim ele passa a ser nuo ate que designem outro valor a ele "c=0" seria o comando aplicavel')
print('os parametros das funções não substituem os numeros apenas os copiam')
print('ha o comando return s que retorna o resultado para variavel')
print('EM CASO DE DUVIDAS VA AO EX120')

print('MODULARIZAÇÃO')
print('a modularização surgiu no inicio da decada de 60 foi criadas para resumir sistemas maiores com o foco de dividr sistemas em pequenos pedaços e tambem tendo a alta legibilidade em foco para que facilite a manutenção')
print('duvidas vá ao ex 127')

print('TRATAMENTO  DE ERROS E CORREÇÕES EM PYTHON')
print('para usar o trataemnto de erros você utiiza o comando "try:" com ele você manda o python tentar solucionar e caso ele não solucione')
print('Logo abaixo do try: vai o "except:" que é caso ele não consiga solucionar o problema o que aconteceria')
print('DUVIDAS VÁ AO EX132')




