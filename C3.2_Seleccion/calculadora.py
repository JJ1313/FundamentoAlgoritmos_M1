n1 = float(input())
operacion = input()
n2 = float(input())

if operacion == "+":
    resultado = n1 + n2
    print(f"resultado = {round(resultado, 1)}")
elif operacion == "-":
    resultado = n1 - n2
    print(f"resultado = {round(resultado, 1)}")
elif operacion == "*":
    resultado = n1 * n2
    print(f"resultado = {round(resultado, 1)}")
else:
    resultado = n1 / n2
    print(f"resultado = {round(resultado, 1)}")
