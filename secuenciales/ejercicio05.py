#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

# Pedir el valor en Fahrenheit
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

# Convertir a Celsius
celsius = (fahrenheit - 32) * 5 / 9;

# Mostrar resultado
print("La temperatura en grados Celsius es:", celsius)
