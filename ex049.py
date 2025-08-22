#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-' * 28)
print('Calculadora de tabuada')
print('-' * 28)
valor = int(input('Digite o valor: '))
for i in range(1, 11):
    tabuada = valor * i
    print(f'{valor} x {i} = {tabuada}')