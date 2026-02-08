#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
#desea saber cuanto deberá pagar finalmente por su compra.





# Programa para calcular el pago final con descuento

# Solicitar el total de la compra
total_compra = float(input("Ingrese el total de la compra: "))

# Calcular el descuento (15%)
descuento = total_compra * 0.15

# Calcular el total a pagar
total_final = total_compra - descuento

# Mostrar resultados
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")