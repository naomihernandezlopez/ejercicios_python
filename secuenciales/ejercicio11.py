#Pide al usuario dos números y muestra la "distancia" entre ellos 
#(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).




# Pedir al usuario dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular la distancia (valor absoluto de la diferencia)
distancia = abs(num1 - num2)

# Mostrar el resultado
print("La distancia entre", num1, "y", num2, "es:", distancia)
