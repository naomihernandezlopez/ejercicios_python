#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
#en cuenta su sueldo base y comisiones.



# Programa para calcular el sueldo total de un vendedor

# Solicitar datos al usuario
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

# Calcular comisiones (10% de cada venta)
comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

# Suma de comisiones
total_comisiones = comision1 + comision2 + comision3

# Sueldo total
sueldo_total = sueldo_base + total_comisiones

# Mostrar resultados
print(f"Comisión por la primera venta: ${comision1:.2f}")
print(f"Comisión por la segunda venta: ${comision2:.2f}")
print(f"Comisión por la tercera venta: ${comision3:.2f}")
print(f"Total de comisiones: ${total_comisiones:.2f}")
print(f"Sueldo total del mes: ${sueldo_total:.2f}")