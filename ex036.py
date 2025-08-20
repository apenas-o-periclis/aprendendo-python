vc = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salario: R$'))
anos = int(input('Em quantos anos voce ira pagar? '))

prestacao = vc / (anos * 12) 
print(f'Sua prestação mensal e de {prestacao:.2f}')

if prestacao > salario * 30/100:
    print('O seu empréstimo foi negado pois a prestação de sua casa esta muito cara!')
else:
    print('Empréstimo realizado. Muito obrigado pela preferencia!')