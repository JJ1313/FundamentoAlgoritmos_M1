# Leer datos
cargoFijo = float(input())
ltsConsumidos = float(input())
valorAgua = float(input())
valorRecolectada = float(input())
valorTratada = float(input())

# Calculo monto total
m3Consumidos = ltsConsumidos / 1000
cargoAgua = m3Consumidos * valorAgua
cargoRecoleccion = m3Consumidos * valorRecolectada
cargoTratamiento = m3Consumidos * valorTratada

montoSinSobrecargo = cargoAgua + cargoRecoleccion + cargoTratamiento + cargoFijo

# Mostra datos
print("BOLETA ESVALPITO")
print(f"Cargo Fijo = ${cargoFijo}")
print(f"Metros cúbicos de agua consumidos = {m3Consumidos}")
print(f"Monto parcial por agua consumida = ${cargoAgua}")
print(f"Monto parcial por agua recolectada = ${cargoRecoleccion}")
print(f"Monto parcial por agua tratada = ${cargoTratamiento}")

# Calculo de sobreconsumo
if m3Consumidos < 40:
    print("Cliente no presenta sobreconsumo")
    montoFinal = montoSinSobrecargo

elif m3Consumidos < 45:
    print("Cliente presenta sobreconsumo, su recargo es de un 15%")
    print(f"Monto Total Antes del recargo = ${montoSinSobrecargo}")
    montoFinal = montoSinSobrecargo * 1.15
elif m3Consumidos < 50:
    print("Cliente presenta sobreconsumo, su recargo es de un 20%")
    print(f"Monto Total Antes del recargo = ${montoSinSobrecargo}")
    montoFinal = montoSinSobrecargo * 1.2
elif m3Consumidos < 65:
    print("Cliente presenta sobreconsumo, su recargo es de un 30%")
    print(f"Monto Total Antes del recargo = ${montoSinSobrecargo}")
    montoFinal = montoSinSobrecargo * 1.3
else:
    print("Cliente presenta sobreconsumo, su recargo es de un 55%")
    print(f"Monto Total Antes del recargo = ${montoSinSobrecargo}")
    montoFinal = montoSinSobrecargo * 1.55

# Imprimir monto total a pagar
print(f"Monto Total a Pagar = ${montoFinal}")
