pt = input('Preço do produto: R$ ')
pc = float(pt) * 5 / 100
print('-' * 40)
print(f'Preço original:      R$ {float(pt):.2f}')
print(f'Desconto de 5%:      R$ {pc:.2f}')
print(f'Preço com desconto:  R$ {float(pt) - pc:.2f}')
print('-' * 40)