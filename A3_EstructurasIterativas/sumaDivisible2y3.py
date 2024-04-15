n1 = int(input())
n2 = int(input())

suma = 0
for i in range(n1, n2 + 1):
    if i % 2 == 0 and i % 3 == 0:
        suma += i

if suma == 0:
    print("NO EXISTEN NUMEROS DIVISIBLES POR 2 Y POR 3 EN EL INTERVALO")
else:
    print(f"SUMA = {suma}")
