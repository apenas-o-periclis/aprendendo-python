#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0
for pes in range(1, 6):
    peso = float(input('Digite o peso da pessoa: '))
    if pes == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso lido foi {maior}')
print(f'o menor peso lido foi {menor}')