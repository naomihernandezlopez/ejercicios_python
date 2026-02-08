#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Evitar división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Mostrar resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)
