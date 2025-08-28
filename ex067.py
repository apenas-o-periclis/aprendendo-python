#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    print('~' * 20)
    num = int(input('Digite o número para descobrir sua tabuada: '))
    if num < 0:
        break
    print('~' * 20)
    print(f''   {num} x 1 = {num * 1}
    {num} x 2 = {num * 2}
    {num} x 3 = {num * 3}
    {num} x 4 = {num * 4}
    {num} x 5 = {num * 5}
    {num} x 6 = {num * 6}
    {num} x 7 = {num * 7}
    {num} x 8 = {num * 8}
    {num} x 9 = {num * 9}
    {num} x 10 = {num * 10}'')
print('O programa foi encerrado. ')
'''

#Eu posso usar um laço for dentro do while, assim como while dentro do while.
while True:
    num = int(input('Digite um número para descobrir sua tabuada: '))
    if num < 0:
        break
    print('^' * 20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c} ')
    print('^' * 20)