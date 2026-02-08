#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
#después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos 
#o 10 céntimos).






# Ingreso de datos
m2e = int(input("Ingrese el número de monedas de 2 euros: "))
m1e = int(input("Ingrese el número de monedas de 1 euro: "))
m50c = int(input("Ingrese el número de monedas de 50 céntimos: "))
m20c = int(input("Ingrese el número de monedas de 20 céntimos: "))
m10c = int(input("Ingrese el número de monedas de 10 céntimos: "))

# Cálculo del total
total = (m2e * 2) + (m1e * 1) + (m50c * 0.5) + (m20c * 0.2) + (m10c * 0.1)

# Separar euros y céntimos
euros = int(total)
centimos = round((total - euros) * 100)

print(f"El dinero total es: {euros} euros y {centimos} céntimos.")