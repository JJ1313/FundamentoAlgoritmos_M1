while True:
    n = int(input())
    if n > 0:
        break
suma = 0
for i in range(n):
    numerador = 2 + 2 * i
    denominador = 1 + 2 * i
    suma += numerador / denominador

print(f"El resultado de la sumatoria es {suma}")
