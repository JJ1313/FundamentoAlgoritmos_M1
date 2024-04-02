temperatura = float(input())

# Opcion 1:
# if temperatura < 20:
#     print("AZUL")
# elif temperatura >= 20 and temperatura < 35:
#     print("AMARILLO")
# else:
#     print("ROJO")

# Opcion2:
""" 
    Como ya revise si es 'temperatura < 20' en el primer if (linea 12),
    no necesito revisar que 'temperatura >= 20'  en el primer elif (linea 14),
    porque ya entra en 'print("AZUL")' si es que es el caso. 
"""
if temperatura < 20:
    print("AZUL")
elif temperatura < 35:
    print("AMARILLO")
else:
    print("ROJO")
