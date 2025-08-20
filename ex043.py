#Desenvolva uma logica que leia o peso e a altura de uma pessoa.
#calcule seu IMC e mostre seu status, de acordo com a tabela a baixo:
#- Abaixo de 18,5:Abaixo do peso
#- Entre 18,5 e 25:peso ideal
#- 25 ate 30:Sobrepeso
#- 30 ate 40:obesidade
#- acima de 40:Obesidade mórbida
alt = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso/(alt * alt)
print('Você está')
if imc <18.5:
    print('abaixo do peso.')
    print(f'seu imc é {imc:.2f}, coma mais!')
elif imc > 18.5 and imc <=25:
    print('No peso ideal.')
    print(f'seu imc é {imc:.2f}, você está saudável, parabéns!!')
elif imc >=25 and imc <= 30:
    print('Acima do peso.')
    print(f'seu imc é {imc:.2f}, comece a se preocupar com sua saúde!')
elif imc >=30 and imc <=40:
    print('Obeso')
    print('\033[0;31mPROCURE AJUDA MÉDICA IMEDIATAMENTE!!')
else:
    print('Em obesidade mórbida.')
    print('\033[0;31mPROCURE AJUDA IMEDIATAMENTE, VOCE CORRE RISCO SÉRIO DE VIDA!!')