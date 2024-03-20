# Leer datos
monto = int(input())
tasaMensual = int(input())

# Calcular ganancia
ganancia = int(monto * tasaMensual / 100)
montoFinal = monto + ganancia

# Mostrar datos

print(f"Monto de dinero invertido = {monto}")
print(f"Tasa de interés mensual = {tasaMensual}%")
print(f"Monto de dinero que ganará el inversionista = {ganancia}")
print(f"Capital actualizado = {montoFinal}")
