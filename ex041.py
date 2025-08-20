#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- ate 9 anos:MIRIM
#- ate 14 anos:INFANTIL
#- ate 19 anos: JUNIOR
#- ate 20 anos: SÊNIOR
#- acima: MASTER

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
print(f'Você tem {idade} anos e:')
if idade <=14:
    print('Você é um nadador MIRIM.')
elif idade <=14 and idade >9:
    print('Você é um nadador INFANTIL.')
elif idade <=19 and idade >14:
    print('Você é um nadador JUNIOR.')
elif idade == 20:
    print('Você é um nadador SÊNIOR.')
else:
    print('Você é um nadador MASTER.')