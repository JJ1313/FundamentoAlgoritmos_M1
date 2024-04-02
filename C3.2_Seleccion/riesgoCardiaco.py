altura = float(input())
peso = int(input())
edad = int(input())

imc = peso / altura**2

print(f"imc = {imc} y edad = {edad}")

if edad < 45:
    if imc < 22:
        print("riesgo cardíaco es bajo")
    else:
        print("riesgo cardíaco es medio")
else:
    if imc < 22:
        print("riesgo cardíaco es medio")
    else:
        print("riesgo cardíaco es alto")
