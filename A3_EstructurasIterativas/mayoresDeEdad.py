n = int(input())
mayoresEdad = 0
for i in range(n):
    edad = int(input())
    if edad >= 18:
        mayoresEdad += 1

if mayoresEdad == 0:
    print("No hubo mayores de edad")
elif mayoresEdad == n:
    print("Todos eran mayores de edad")
else:
    print(f"Cantidad de mayores de edad: {mayoresEdad}")
