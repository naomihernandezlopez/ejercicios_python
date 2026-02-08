#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
#Si introducimos otro número nos da un error.




# Programa para mostrar los días de un mes

# Entrada de datos
mes = int(input("Introduce el número de mes (1-12): "))

# Determinamos los días del mes
if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("31 días")
elif mes in [4, 6, 9, 11]:
    print("30 días")
elif mes == 2:
    print("28 o 29 días")
else:
    print("Mes incorrecto")