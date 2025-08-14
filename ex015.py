print('-' * 40)
print('   Calculadora de Aluguel de Carros')
print('-' * 40)

km = float(input('Quantos km você andou? '))
dias = float(input('Quantos dias esteve com o carro? '))

aluguel = 60 * dias + 0.15 * km

print('-' * 40)
print(f'O preço a se pagar é de: R$ {aluguel:.2f}')
print('-' * 40)
