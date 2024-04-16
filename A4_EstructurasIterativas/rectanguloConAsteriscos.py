altura = int(input())
ancho = int(input())

for i in range(altura):  # Recorren las filas
    for i in range(ancho):  # Recorren columnas de cada fila
        print("*", end="")
    print()  # Salto de linea para la siguiente fila
