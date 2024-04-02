n1 = int(input())
n2 = int(input())

if n1 > 10 and n2 > 10:
    print("Ambos son mayores a 10")
elif n1 > 10:
    print(f"{n1} es mayor a 10")
elif n2 > 10:
    print(f"{n2} es mayor a 10")
else:
    print("Ninguno es mayor a 10")
