# Leer datos
ninas = int(input())
ninos = int(input())

# Calcular porcentajes
totalEstudiantes = ninas + ninos

porcentajeNinas = 100 * (ninas / totalEstudiantes)
porcentajeNinos = 100 * (ninos / totalEstudiantes)

# Mostrar datos
print(f"Porcentaje de Niñas en el curso = {porcentajeNinas}%")
print(f"Porcentaje de Niños en el curso = {porcentajeNinos}%")
