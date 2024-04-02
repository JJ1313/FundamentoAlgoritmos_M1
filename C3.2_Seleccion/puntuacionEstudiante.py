n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

promedio = (n1 + n2 + n3 + n4) // 4

print(f"promedio = {promedio}")
if promedio <= 59:
    print("nota final = E")
elif promedio <= 69:
    print("nota final = D")
elif promedio <= 79:
    print("nota final = C")
elif promedio <= 89:
    print("nota final = B")
else:
    print("nota final = A")
