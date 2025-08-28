#Crie um programa que leia vários numeros inteiros pelo teclado no final do programa, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = int(input('Digite um número para começar a somar: '))
soma = num
continuar = 's'
cont = 1
maior = num #Variáveis que precisam ser atualizada correntemente precisam começar fora do laço
menor = num ##Variáveis que precisam ser atualizada correntemente precisam começar fora do laço
while continuar == 's':
    num = int(input('Digite mais um número: '))
    soma += num
    continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()[0]
    if num < menor:
        menor = num #O menor quem recebe num, nao o contrario
    if num > maior:
        maior = num #O maior quem recebe num, nao o contrario
    cont += 1
print(f'Você digitou {cont} valores, a soma total foi: {soma}, a média foi {soma / cont:.2f}, o maior número digitado foi {maior} e o menor número digitado foi {menor}')
    