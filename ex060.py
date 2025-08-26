#faça um programa que leia um número qualquer e mostre o seu fatorial 
#ex: 5! = 5x4x3x2x1 = 120
num = int(input('Digite um número para descobrir seu fatorial: '))
cont = num
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont >1 else ' = ', end='')
    f = f * cont
    cont = cont - 1
print(f)
