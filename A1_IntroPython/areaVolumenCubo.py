# Leer datos
lado = float(input())

# Calcular area y volumen
area = lado * lado * 6  # Area -> opcion 1
# area = lado**2 * 6  # Area -> opcion 2

volumen = lado * lado * lado  # Volumen -> opcion 1. muestra mas decimales
volumen = lado**3  # Volumen -> opcion 2

print("área del cubo =", area)
print("volumen del cubo =", volumen)
