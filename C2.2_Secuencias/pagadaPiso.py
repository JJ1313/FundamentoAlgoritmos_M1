cantPersonas = int(input())
cantPasteles = int(input())
precioPastel = int(input())
cantBebidas = int(input())
precioBebida = int(input())

totalItems = cantPasteles + cantBebidas
totalGastado = cantPasteles * precioPastel + cantBebidas * precioBebida
montoCuota = round(totalGastado / cantPersonas)

print(f"Total items comprados : {totalItems}")
print(f"Total gastado en pasteles y bebidas : {totalGastado}")
print(f"Monto a pagar por cada uno : {montoCuota}")