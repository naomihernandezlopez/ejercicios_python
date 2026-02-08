#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.






# Ingreso de datos
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

# Obtener iniciales
iniciales = nombre[0] + apellido1[0] + apellido2[0]

print("Las iniciales son:", iniciales.upper())