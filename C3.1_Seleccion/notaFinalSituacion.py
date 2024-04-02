n1 = float(input())
n2 = float(input())
n3 = float(input())

promedio = round((n1 + n2 + n3) / 3, 2)

print(f"Promedio = {promedio}")
if promedio >= 4.0:
    print("Aprobaste la Asignatura")
else:
    print("Reprobaste la Asignatura")