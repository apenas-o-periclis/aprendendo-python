#Desenvolva um programa que perguntte a distancia de uma viagem em km.
#Calcule o preco da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 pra viagens mais longas
viagem = float(input('Quantos km tem sua viagem?: '))
vl = viagem * 0.45
vc = viagem * 0.50

if viagem <=200:
    print(f'o preco a se pagar e de R${vc}.')
else:
    print(f'o preco a se pagar e de R${vl}.')