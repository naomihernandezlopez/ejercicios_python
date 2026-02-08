#La asociación de vinicultores tiene como política fijar un precio inicial 
# al kilo de uva, la cual se clasifica en tipos A y B,  y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
#se requiere determinar cuánto recibirá un productor por la uva que entrega en un 
#embarque, considerando lo siguiente: 
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es 
# de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos 
# cuando es de tamaño 2. 
# Realice un algoritmo para determinar la ganancia obtenida.






# Programa para calcular la ganancia por venta de uvas

# Entrada de datos
precio_inicial = float(input("Introduce el precio inicial por kilo de la UVA (en céntimos): "))
kilos = int(input("Introduce cuántos kilos has vendido: "))
tipo = input("Introduce el tipo de la UVA (A/B): ").upper()

# Validación del tipo
if tipo not in ["A", "B"]:
    print("Tipo incorrecto.")
else:
    tamano = input("Introduce el tamaño de la UVA (1/2): ")

    # Validación del tamaño
    if tamano not in ["1", "2"]:
        print("Tamaño incorrecto.")
    else:
        # Ajuste del precio según tipo y tamaño
        if tipo == "A":
            if tamano == "1":
                precio_inicial += 20
            else:  # tamaño 2
                precio_inicial += 30
        else:  # tipo B
            if tamano == "1":
                precio_inicial -= 30
            else:  # tamaño 2
                precio_inicial -= 50

        # Cálculo de ganancia
        precio_final = precio_inicial * kilos
        print("La ganancia es", precio_final / 100, "euros.")