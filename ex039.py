#faca um programa que leia o ano dos nascimento de um jovem e informe, de acordo com sua idade:
#- se ele ainda vai se alistar ao servico militar.
#- se é hora dele se alistar
#- se ele ja passou do tempo do alistamento
#seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

nascimento = int(input('em qual ano voce nasceu? '))
atual = date.today().year
idade = atual - nascimento
print(f'voce tem {idade} anos, e:')
if idade == 18:
    print('ja esta na hora de se alistar! ')
elif idade > 18:
    faltam = date.today().year - (idade - 18)
    print(f'Você ja deveria ter se alistado, seu alistamento foi em {faltam}.')
else:
    faltam = date.today().year + (18 - idade)
    print(f'Você deve se alistar em {faltam}.')