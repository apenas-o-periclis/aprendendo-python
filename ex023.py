num = int(input('escolha um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num// 1000 % 10
print(f' unidade do seu numero: {u}\n dezena do seu numero: {d}\n centena do deu numero: {c}\n milhar do seu numero: {m}')