# Leer cantidad bebidas
cantBebidas = int(input())

# Calcular jabas

cantJabas = cantBebidas // 12  # Opcion 1
cantJabas = int(cantBebidas / 12)  # Opcion 2

botellasSobran = cantBebidas % 12

print(f"Cantidad de jabas = {cantJabas}")
print(f"quedan {botellasSobran} sin trasladar")
