# Conversor de Temperatura: Celsius para Fahrenheit

print("=== Conversor de Temperatura ===")
celsius = float(input("Quantos graus Celsius está hoje? "))
fahrenheit = celsius * 9 / 5 + 32 #Formula para transformas graus celsius em fahrenheit
print(f"{celsius:.1f}°C corresponde a {fahrenheit:.1f}°F")
