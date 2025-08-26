#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep

num1 = float(input('Escolha um número: '))
num2 = float(input('Escolha outro número: '))
opção = int(input('''Selecione a operação:
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
while opção != 5:
    if opção == 1:
        print(num1 + num2)
        opção = int(input('''Selecione a operação: 
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
    if opção == 2:
        print(num1 * num2)
        opção = int(input('''Selecione a operação: 
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
    if opção == 3:
        if num1 > num2:
            print(num1)
            opção = int(input('''Selecione a operação: 
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
        else:
            print(num2)
            opção = int(input('''Selecione a operação: 
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
    if opção == 4:
        num1 = float(input('Escolha um número: '))
        num2 = float(input('Escolha outro número: '))
        opção = int(input('''Selecione a operação: 
                  [1] Somar 
                  [2] Multiplicar
                  [3] Descobrir o maior
                  [4] Novos números
                  [5] Sair do programa
                  Sua opção: '''))
    else:
        print('opção inválida, tente novamente. ')
        sleep(1)
    num1 = float(input('Escolha um número: '))
    num2 = float(input('Escolha outro número: '))
    opção = int(input('''Selecione a operação: 
[1] Somar 
[2] Multiplicar
[3] Descobrir o maior
[4] Novos números
[5] Sair do programa
Sua opção: '''))
        
print('O programa encerrou')