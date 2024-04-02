from math import trunc
n = float(input())

print(f"Numero Redondeado = {round(n)}")
# print(f"Numero Truncado = {trunc(n)}") # Usando trunc de libreria math
print(f"Numero Truncado = {int(n)}") # Usando casting (convertir un tipo de dato a otro) -> No es necesario importar (linea 1)

