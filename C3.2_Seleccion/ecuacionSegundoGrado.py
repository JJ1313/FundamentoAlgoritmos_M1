a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if a == 0:
    print("No es una ecuación de segundo grado")

elif d > 0:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print(f"x1 = {round(x1, 1)}")
    print(f"x2 = {round(x2, 1)}")

elif d == 0:
    x = -b / (2 * a)
    print(f"x = {round(x, 1)}")

else:
    print("La ecuación tiene raíces complejas")
