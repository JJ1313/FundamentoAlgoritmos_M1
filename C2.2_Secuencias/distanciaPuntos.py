from math import sqrt # Para usar sqrt de libreria math
# Leen datos
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# Calcula distancia
d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2) # Solucion sin libreria math -> No es necesario importar (linea 1)

# Muestra resultados
print(f"La distancia total es de {round(d, 1)}")