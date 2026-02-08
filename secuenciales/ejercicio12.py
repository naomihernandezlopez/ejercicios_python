#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
#en el plano. Calcula y muestra la distancia entre ellos.





# Programa para calcular la distancia entre dos puntos en el plano

import math

# Pedir al usuario las coordenadas del primer punto
x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))

# Pedir al usuario las coordenadas del segundo punto
x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))

# Calcular la distancia usando la fórmula de distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado
print("La distancia entre los puntos (", x1, ",", y1, ") y (", x2, ",", y2, ") es:", distancia)