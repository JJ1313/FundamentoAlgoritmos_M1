while True:
    n = int(input())
    if n > 0 and n < 21:
        break

# Opcion 1
for i in range(n):  # Recorro filas
    for j in range(
        i + 1
    ):  # En la fila n necesito n asteriscos, fila 3 hay 3 asteriscos
        print("*", end="")
    print()

# Opcion 2
# for i in range(1, n+1): # Recorro filas
#     for j in range(i): # En la fila n necesito n asteriscos, fila 3 hay 3 asteriscos
#         print("*", end='')
#     print()
