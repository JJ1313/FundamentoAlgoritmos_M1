# Lectura de datos
episodio = int(input())
nivel = int(input())
puntajeMinimo = int(input())
puntajeObtenido = int(input())
vidas = int(input())

# CONDICIONES

# NO pasa el nivel
if puntajeObtenido < puntajeMinimo:
    print("Nivel no superado NO lograste el objetivo")
    vidas -= 1
    if vidas == 0:
        print("No te quedan más vidas.")
    elif vidas == 1:
        print(f"Te queda {vidas} vida.")
    else:
        print(f"Te quedan {vidas} vidas.")

# SI pasa el nivel
else:
    print("Genial nivel superado !")

    # Calculo de estrellas

    # Opcion 1 - calculo estrellas
    razon = puntajeObtenido / puntajeMinimo
    if razon < 2:
        estrellas = 1
    elif razon < 3:
        estrellas = 2
    else:
        estrellas = 3

    # Opcion 2 - calculo estrellas
    # estrellas = min(puntajeObtenido // puntajeMinimo, 3)

    # Imprimir mensaje de estrellas
    if estrellas > 1:
        print(f"Obtuviste {estrellas} estrellas.")
    else:
        print(f"Obtuviste {estrellas} estrella.")

    # Imprimir mensaje de nivel o episodio superado
    nivel += 1
    if nivel == 16:
        print(f"Completaste el episodio {episodio}")
    else:
        print(f"Pasaste al nivel {nivel} del episodio {episodio}")
