#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s = s + n
print(f'A soma de todos os valores solicitados é {s}')
