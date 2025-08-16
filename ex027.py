nome = str(input('digite seu nome: ')).strip().lower()
n = nome.split()
print(f'seu primeiro nome e {n[0]}')
print(f'seu ultimo nome e {n[len(n) - 1]}')