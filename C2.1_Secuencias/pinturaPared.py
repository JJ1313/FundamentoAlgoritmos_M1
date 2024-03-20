# Leer datos
alto = int(input())
ancho = int(input())
cantManos = int(input())
mts2xL = int(input())

# Calcular
superficie = alto * ancho
cantLitros = superficie * cantManos / mts2xL

# Mostrar datos
print(f"Superficie Pared = {superficie} m2")
print(f"Manos de Pintura = {cantManos}")
print(f"Metros Cuadrados por Litro de Pintura = {mts2xL}")
print(f"Humberto necesitas comprar {cantLitros} litro(s) de pintura")
