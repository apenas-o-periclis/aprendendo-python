#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais. 
#o aumento é de 15%.

salario = float(input('digite seu salario atual: '))
if salario <=1250.00:
    aumento = salario * 15/100
    print(f'seu noco salario com aumento de 15% e de {salario + aumento}')
else:
    aumento = salario * 10/100
    print(f'o seu novo salario com aumento de 10% e de {salario + aumento}')