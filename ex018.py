import math
an=float(input('digito o angulo: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'o angulo {an} tem o SENO equivalente a {seno:.2f}\no COSSENO equivalente a {cosseno:.2f}\ne a TANGENTE equivalente a {tan:.2f}')