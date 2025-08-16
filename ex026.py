frase = str(input('digite a sua frase: ')).strip().lower()
print(f'A letra A aparece: {frase.count('a')} vezes')
print(f'a perimeira letra A aparece em qual posicao? {frase.find('a') + 1}')
print(f'a ultima letra A aparece em qual posicao {frase.rfind('a') + 1 - frase.count(' ')}')