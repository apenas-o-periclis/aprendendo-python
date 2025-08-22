#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from emoji import emojize
print('-=' * 18)
print('Contagem regressiva para o estouro!')
print('-=' * 18)

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOOOOOOOOMMMMMMMMMM' + emojize('💥💥💥'))