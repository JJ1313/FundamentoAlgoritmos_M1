salario = int(input())

if salario < 250000:
    nuevoSalario = salario * 1.2
elif salario < 500000:
    nuevoSalario = salario * 1.1
elif salario < 1000000:
    nuevoSalario = salario * 1.05
else:
    nuevoSalario = salario

print(f"Salario reajustado = $ {round(nuevoSalario)}")
