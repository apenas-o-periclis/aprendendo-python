#escreva um programa que leia velocidade de um carro.
#se ele ultrapassar 80km/h, mostre uma mennsagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cara km acima do limite

velocidade = float(input('digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'voce foi multado! a multa equivale a R${multa:.2f}')
print('Tenha um bom dia e dirija com sseguranca')