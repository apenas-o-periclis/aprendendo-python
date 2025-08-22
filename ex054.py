#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
        nascimento = int(input('Digite a sua data de nascimento: '))
        idade = atual - nascimento
        if idade >=18:
            maiores += 1
        else:
            menores += 1
print(f'O número de maiores de idade foi {maiores}')
print(f'O número de menores de idade foi {menores}')

