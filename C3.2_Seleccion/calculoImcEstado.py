peso = float(input())
altura = float(input())

imc = peso / altura**2
print(f"imc paciente = {round(imc, 1)}")

if imc < 16.5:
    print(f"Estado nutricional paciente : Desnutrición")
    print("Alerta : paciente debe modificar su dieta alimenticia")
elif imc < 18.5:
    print(f"Estado nutricional paciente : Delgadez")
    print("Alerta : paciente debe mantener su dieta alimenticia")
elif imc < 25:
    print(f"Estado nutricional paciente : Peso Normal")
    print("Alerta : paciente debe mantener su dieta alimenticia")
elif imc < 30:
    print(f"Estado nutricional paciente : Sobrepeso")
    print("Alerta : paciente debe modificar su dieta alimenticia")
elif imc < 40:
    print(f"Estado nutricional paciente : Obesidad Moderada")
    print("Alerta : paciente debe modificar su dieta alimenticia")
else:
    print(f"Estado nutricional paciente : Obesidad Mórbida o Masiva")
    print("Alerta : paciente debe modificar su dieta alimenticia")
