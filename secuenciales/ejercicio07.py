#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.


# Programa que convierte minutos a horas y minutos

# Solicitar al usuario la cantidad de minutos
minutos = int(input("Ingrese la cantidad de minutos: "))

# Calcular horas y minutos
horas = (minutos / 60)
resto_minutos = minutos % 60

# Mostrar el resultado
print(f"{minutos} minutos equivalen a {horas} horas y {resto_minutos} minutos.")