#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.


import math


cateto1 = float(input("Ingresa el valor del primer cateto: "))
cateto2 = float(input("Ingresa el valor del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostrar resultado
print("La hipotenusa del triángulo es:", hipotenusa)
