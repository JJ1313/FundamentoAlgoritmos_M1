# Leer Datos
bebidas = int(input())
precioBebidas = int(input())

pizzas = int(input())
precioPizzas = int(input())

palomitas = int(input())
precioPalomitas = int(input())

invitados = int(input())

# Calcular datos
totalGastos = (
    bebidas * precioBebidas + pizzas * precioPizzas + palomitas * precioPalomitas
)
valorCuota = round(totalGastos / invitados)
totalItems = bebidas + pizzas + palomitas

# Mostrar Resultados
print(f"Total gasto compra = {totalGastos}")
print(f"Valor cuota por invitado = {valorCuota}")
print(f"Total items comprados = {totalItems}")
