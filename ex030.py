#Crie um programa que leia um numero inteiro e mostre na tela de ele e par ou impar

num = int(input('digite um numero: '))
resultado = num % 2
if resultado == 1:
    print('E ele e impar')
else:
    print('E ele e par')