# Leer datos
patente = input()
categoria = int(input())
tarifa = input()
kms = float(input())

# Calcular valor peaje
if categoria == 1:
    if tarifa == "BAJA":
        costoKm = 90
    elif tarifa == "MEDIA":
        costoKm = 90 * 2
    else:
        costoKm = 90 * 3
elif categoria == 2:
    if tarifa == "BAJA":
        costoKm = 360 / 2
    elif tarifa == "MEDIA":
        costoKm = 360
    else:
        costoKm = 3 * 360 / 2

elif categoria == 3:
    if tarifa == "BAJA":
        costoKm = 780 / 3
    elif tarifa == "MEDIA":
        costoKm = 2 * 780 / 3
    else:
        costoKm = 780

else:
    if tarifa == "BAJA":
        costoKm = 100
    elif tarifa == "MEDIA":
        costoKm = 3 * 100
    else:
        costoKm = 5 * 100

valorPeaje = int(costoKm * kms)

# Imprimir datos sin descuento
print(f"Vehículo Placa Patente : {patente}")
print(f"Categoría del Vehículo : {categoria}")
print(f"Categoría Tarifa : {tarifa}")
print(f"Distancia recorrida por el vehículo = {kms} kms.")
print(f"Valor del peaje calculado es ${valorPeaje}")


# Calculo y mostrar de descuento
if valorPeaje < 2000:
    print("No se aplica descuento")
elif valorPeaje < 5000:
    print("Se aplica descuento del 7%")
    print(f"Valor Final del peaje a pagar es ${int(valorPeaje * 0.93)}")
elif valorPeaje <= 10000:
    print("Se aplica descuento del 12%")
    print(f"Valor Final del peaje a pagar es ${int(valorPeaje * 0.88)}")
else:
    print("Se aplica descuento del 15%")
    print(f"Valor Final del peaje a pagar es ${int(valorPeaje * 0.85)}")
