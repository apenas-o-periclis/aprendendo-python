#escreva um programa que leia doi numero inteiros e compare-os.
#mostrando na tela uma mensagem:
#- o primeiro valor e maior.
#- o segundo valor e o maior.
#- nao existe valor maior, os dois sao iguais.

num1 = int(input('Digite um número: '))

num2 = int(input('Digite outro número: '))

print(f'Numeros digitados: {num1} e {num2}')

if num1 > num2:
    print('O primeiro número é o maior.')

elif num1 < num2:
    print('O segundo número é o maior.')

else:
    print('Não existe número maior, os dois são iguais.')