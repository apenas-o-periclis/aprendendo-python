#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 13)
print('Analisador de triângulos.')
print('-=' * 13)

r1 = float(input('digite a primeira reta: '))
r2 = float(input('digite a segunda reta: '))
r3 = float(input('digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print ('essas retas PODEM formar um triangulo.')
else:
    print ('essas retas NAO PODEM formas um triangulo.')