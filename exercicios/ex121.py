def voto(ano):
    from datetime import date
    anoatual = date.today().year
    id = anoatual - ano
    if id < 16:
        print(f'Você tem {id} anos e NÃO VOTA')
    elif id >= 18:
        print(F'Você tem {id} anos  O VOTO É OBRIGATORIO')
    elif 16 <= id < 18 or id > 65:
        print(F'Você tem {id} anos O VOTO É OPCIONAL')


voto(int(input('Em qual ano você nasceu ?')))
