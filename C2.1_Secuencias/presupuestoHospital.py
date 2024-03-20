# Leer datos
presupuesto = int(input())

# Porcentajes
urgenciax100 = 37
pediatriax100 = 42
traumatologiax100 = 21

# Calcular presupuesto areas
presupuestoUrgencia = int(urgenciax100 * presupuesto / 100)
presupuestoPediatria = int(pediatriax100 * presupuesto / 100)
presupuestoTraumatologia = int(traumatologiax100 * presupuesto / 100)

# Mostrar datos
print(f"Presupuesto Área Urgencia = ${presupuestoUrgencia}")
print(f"Presupuesto Área Pediatría = ${presupuestoPediatria}")
print(f"Presupuesto Área Traumatología = ${presupuestoTraumatologia}")
