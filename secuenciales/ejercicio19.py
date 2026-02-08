#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
#por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
#blanco 0. Imprime el resultado obtenido por el estudiante.






# Ingreso de datos
correctas = int(input("Ingrese el número de respuestas correctas: "))
incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
blanco = int(input("Ingrese el número de respuestas en blanco: "))

# Cálculo de la nota final
nota = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

print("La nota final del estudiante es:", nota)