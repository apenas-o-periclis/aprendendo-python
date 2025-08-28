#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from emoji import emojize
from random import randint
print('Vamos jogar par ou ímpar!')
cont = 0
while True:
    num = int(input('Escolha um número: '))
    while num > 10:
        print(f'Você realmente tem {num} dedos? + {emojize('🤣')}')
        num = int(input('Escolha um número: '))
    comp_num = randint(1,10)
    pi = str(input('Par ou Ímpar: [P/I]')).strip().lower()[0]
    while pi not in 'IiPp':
        print('Opção inválida, tente novamente. ')
        pi = str(input('Par ou Ímpar: [P/I]')).strip().lower()[0]
    if pi == 'p':
        comp_pi = 'i'
    elif pi == 'i':
        comp_pi = 'p'
    num_pi = (num + comp_num) % 2
    if num_pi == 0 and pi == 'p':
        print(f'Voce Venceu, eu escolhi o número {comp_num} e {comp_pi}, a soma foi {comp_num + num}')
        cont +=1
    elif num_pi == 0 and pi == 'i':
        print(f'Voce perdeu, eu escolhi o número {comp_num} e {comp_pi}, a soma foi {comp_num + num}')
        break
    if num_pi != 0 and pi == 'i':
        print(f'Voce Venceu, eu escolhi o número {comp_num} e {comp_pi}, a soma foi {comp_num + num}')
        cont +=1
    elif num_pi != 0 and pi == 'p':
        print(f'Voce perdeu, eu escolhi o número {comp_num} e {comp_pi}, a soma foi {comp_num + num}')
        break
print('Fim de jogo.')

print(f'Você venceu {cont} vezes consecutivas, parabéns!')
