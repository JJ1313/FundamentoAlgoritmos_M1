while True:
    n = int(input())
    if n >= 1:
        break

suma = 0
for i in range(n):
    numerador = 1 + 3 * i
    denominador = 2 + 3 * i
    suma += numerador / denominador

print(f"El resultado de la sumatoria es {suma}")
