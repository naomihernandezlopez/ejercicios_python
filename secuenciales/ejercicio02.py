#Calcular el perimetro y área de un rectángulo dada su base y su altura

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Calcular área y perímetro
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar resultados
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)
