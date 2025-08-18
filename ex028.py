# Exercício: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

es = int(input('Escolha um número entre 0 e 5: '))
ec = random.randrange(0, 5)
if es == ec:
    print(f'Você venceu! Eu realmente escolhi {ec}.')
else:
    print(f'Você perdeu! O meu número era {ec}.')
