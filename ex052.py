#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from math import sqrt
n = int(input('Digite um número: '))
eh_primo = True  # assume que é primo até provar o contrário

if n < 2:
    eh_primo = False
else:
    for c in range(2, int(sqrt(n)) + 1):
        if n % c == 0:
            eh_primo = False
            break

if eh_primo:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')