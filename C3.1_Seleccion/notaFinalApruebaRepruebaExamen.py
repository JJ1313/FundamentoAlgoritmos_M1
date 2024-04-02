n1 = float(input())
n2 = float(input())
n3 = float(input())

promedio = (n1 + n2+ n3) / 3
promedio = round(promedio, 2)

print(f"Promedio = {promedio}")
if promedio < 3:
    print("Reprobaste la asignatura")
elif promedio >= 6.5:
    print("Aprobaste la asignatura")
else:
    print("Debes rendir examen final en esta asignatura")