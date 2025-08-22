#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
cont = t
for c in range(1, 11):
    print(cont, end=' -> ')
    cont = cont + r
print('Acabou')