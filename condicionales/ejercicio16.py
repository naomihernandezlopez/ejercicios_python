#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.



# Programa para calcular el coste de una llamada telefónica

# Entrada de datos
tiempo = int(input("¿Cuánto tiempo es la llamada (en minutos)?: "))
es_domingo = input("¿Es Domingo? (S/N): ").upper()
turno = ""

if es_domingo == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T): ").upper()

# Cálculo del coste base en céntimos
if tiempo <= 5:
    coste = tiempo * 100
elif tiempo <= 8:
    coste = (tiempo - 5) * 80 + 500
elif tiempo <= 10:
    coste = (tiempo - 8) * 70 + 240 + 500
else:
    coste = (tiempo - 10) * 50 + 140 + 240 + 500

# Aplicación de impuestos
if es_domingo == "S":
    coste = coste + coste * 0.03
else:
    if turno == "M":
        coste = coste + coste * 0.15
    else:
        coste = coste + coste * 0.10

# Resultados
print("El coste de la llamada es:", round(coste / 100, 2), "euros.")