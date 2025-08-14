largura = float(input('Qual a largura da parede (m)? '))
altura = float(input('Qual a altura da parede (m)? '))

area = largura * altura
litros_tinta = area / 2

print(f'Área da parede: {area:.2f} m²')
print(f'Você precisará de {litros_tinta:.2f} litros de tinta para pintar a parede.')