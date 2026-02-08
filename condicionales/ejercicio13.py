

#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.




# Programa para verificar si una fecha es correcta

# Entrada de datos
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))

# Inicializamos variable
dias_del_mes = 0

# Determinamos los días según el mes
if mes in [1, 3, 5, 7, 8, 10, 12]:
    dias_del_mes = 31
elif mes in [4, 6, 9, 11]:
    dias_del_mes = 30
elif mes == 2:
    # Verificamos si el año es bisiesto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("Fecha incorrecta (mes inválido).")
    exit()

# Validamos el día
if dia <= 0 or dia > dias_del_mes:
    print("Fecha incorrecta.")
else:
    print("Fecha correcta.")