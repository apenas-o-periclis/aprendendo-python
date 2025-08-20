#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- a vista dinheiro/cheque: 10% de desconto
#- a vista no cartão: 5% de desconto
#- em ate 2x no cartão:preço normal
#- 3x ou mais no cartão: 20% de juros

produto = float(input('Qual é o valor do produto? R$'))
condição = int(input('''Digite uma opção para selecionar a condição de pagamento:
[1] a vista no dinheiro (10% de desconto)
[2] a vista no cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão (20% de juros)
Sua opção: '''))
if condição == 1:
    desconto = produto * 10/100
    print(f'Seu produto custará R${produto - desconto:.2f} com 10% de desconto.')
elif condição == 2:
    desconto = produto * 5/100
    print(f'seu produto custará R${produto - desconto:.2f} com 5% de desconto.')
elif condição == 3:
    parcelas = produto /2
    print(f'seu produto custará R${produto:.2f} em parcelas de R${parcelas:.2f}')
elif condição == 4:
    num_de_parcelas = int(input('Em quantas parcelas irá pagar? '))
    juros = produto + (produto * 20/100)
    parcelas = juros / num_de_parcelas
    print(f'Seu produto custara R${juros:.2f} com juros de 20%, em parcelas de R${parcelas:.2f}.')