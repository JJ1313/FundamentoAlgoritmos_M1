a = float(input())
b = float(input())
c = float(input())

# Triangulo NO valido
if a + b <= c or a + c <= b or b + c <= a:
    print("No es un triángulo")

# Triangulo valido
else:
    # Equilatero
    if a == b and b == c:
        print("Si es un triángulo")
        print("El triángulo es equilátero")
    # Escaleno
    elif a != b and a != c and b != c:
        print("Si es un triángulo")
        print("El triángulo es escaleno")
    # Isosceles
    else:
        print("Si es un triángulo")
        print("El triángulo es isósceles")
