# import math # Hay que usar math.sqrt()
from math import sqrt  # sqrt sin math.

# Leer catetos
a = float(input())
b = float(input())

# Calcular hipotenusa
c = (a**2 + b**2) ** (1 / 2)  # Opcion 1
c = sqrt(a**2 + b**2)  # Opcion 2

# Mostrar resultado

print(round(c, 1))
