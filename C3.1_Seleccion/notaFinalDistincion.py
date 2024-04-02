n1 = float(input())
n2 = float(input())
n3 = float(input())

promedio = (n1 + n2 + n3) / 3
promedio = round(promedio, 2)

print(f"Promedio = {promedio}")

if promedio >= 6:
    print("Felicitaciones Aprobaste con Distinción")
    
print("Felices vacaciones !!")