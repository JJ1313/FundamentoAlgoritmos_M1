peso = float(input())
altura = float(input())

imc = peso / altura ** 2
imc = round(imc, 1)

print(f"imc paciente = {imc}")
if imc >= 25 or imc < 16.5:
    print("Alerta : paciente debe modificar su dieta alimenticia")