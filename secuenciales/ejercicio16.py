#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
#por una distancia d. 
#El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo 
#para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
#velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
#alcanzará el vehículo más rápido al otro.





# Ingreso de datos
d = float(input("Ingrese la distancia entre los vehículos (km): "))
v1 = float(input("Ingrese la velocidad del vehículo delantero (km/h): "))
v2 = float(input("Ingrese la velocidad del vehículo trasero (km/h): "))

# Validación
if v2 <= v1:
    print("El vehículo trasero no alcanzará al delantero.")
else:
    tiempo_min = (d / (v2 - v1)) * 60
    print("El vehículo más rápido alcanzará al otro en", tiempo_min, "minutos.")