# Leer datos
precio = int(input())
porcentajeDescuento = int(input())

# Calcular descuento
descuento = int(precio * porcentajeDescuento / 100)
montoFinal = precio - descuento

# Mostrar datos
print(f"Monto Total Medicamentos = {precio}")
print(f"Porcentaje de descuento = {porcentajeDescuento}%")
print(f"Monto de descuento = {descuento}")
print(f"Monto Total a Pagar = {montoFinal}")
