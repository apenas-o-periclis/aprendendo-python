#8:Crie um programa que faca o computador jogar jokenpo com voce.
import random
player = str(input('Escolha entre pedra papel e tesoura: ')).strip().lower()
python = random.choice(['pedra', 'papel', 'tesoura'])

if player == 'tesoura' and python == 'papel' or player == 'papel' and python == 'pedra' or player == 'pedra' and python == 'tesoura':
    print(f'Você venceu!, minha escolha foi {python}')
elif player != 'pedra' and player !='tesoura' and player != 'papel':
    print(f'Não existe {player} no jokenpo, jogue direito!!')
else:
    print(f'Eu venci!, eu escolhi {python}')