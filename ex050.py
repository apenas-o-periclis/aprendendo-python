#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for num in range(1, 7):
    n = int(input('Digite un número: '))
    if n % 2 == 0:
        soma = soma + n
print(soma)