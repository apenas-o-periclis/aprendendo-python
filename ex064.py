#Crie um programa que leia vários numeros inteiros pelo teclado. o programa so vai para quando o usúario digitar o valor 999, que é condição de parada. no final, mostre quantos npumeros foram digitados e qual foi o soma entre eles (desconsiderando o flag = 999)
from sys import set_int_max_str_digits
set_int_max_str_digits(10000000)
num = int(input('Digite um valor para adicionar a soma (999 para parar): '))
flag = 999
soma = 0
while flag != num:
    soma = soma + num
    print(f'Soma até o momento é {soma}')
    num = int(input('Digite um valor para adicionar a soma (999 para parar): '))
print(soma)