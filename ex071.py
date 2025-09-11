#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor a sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced: #Preciso comparar o total com a cédula atual.
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f'{totalced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20: #Condições alinhadas com elifs, não ifs
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Acabou')