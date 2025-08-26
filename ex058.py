#Melhore o jogo do desafio 028, ondae o computador vai 'pensar' em um número entre 0 10. só que agora o jogador vai tentar adivinhar até, mostrando no final quanttos palpites forram necessarios para vencer.
from random import randint
computador = randint(1, 10)
palpites = 0
palpite = int(input('Escolha um número de 1 a 10: '))
while computador != palpite:
    if palpite < computador:
        print('Um pouco mais... Tente de novo')
    else:
        print('Um pouco menos... Tente de novo')
    palpite = int(input('Escolha um número de 1 a 10: '))
    palpites = palpites + 1
print(f'Você acertou e levou {palpites + 1} palpites')