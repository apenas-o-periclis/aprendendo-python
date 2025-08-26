#escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
#ex 0 -> 1 -> 1 -> 2 ->3 -> 5 -> 8

n = int(input('Digite um número: '))

cn = n
cont = 0
n1 = 0
n2 = 1
while cont <n:
    print(n1, end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont +=1
