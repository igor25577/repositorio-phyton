palavra = str(input("Digite qualquer palavra ou frase, e irei verificar se nela tem a letra A seja maiuscula ou minuscula e quantas vezes a letra aparece:")
)
palavra_mai = palavra.upper()
cont_l = palavra_mai.count('A')

if cont_l > 0:
    print(f"A letra 'a' aparece {cont_l} vezes na palavra/frase digitada.")
else:
    print(f"A letra 'a' não foi encontrada na string.")     