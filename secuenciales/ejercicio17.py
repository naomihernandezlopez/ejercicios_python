#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.




# Ingreso de datos
HH = int(input("Ingrese la hora de partida (HH): "))
MM = int(input("Ingrese los minutos de partida (MM): "))
SS = int(input("Ingrese los segundos de partida (SS): "))
T = int(input("Ingrese el tiempo de viaje en segundos (T): "))

# Conversión a segundos totales
seg_inicial = HH*3600 + MM*60 + SS
seg_final = seg_inicial + T

# Conversión a HH:MM:SS
HH = (seg_final // 3600) % 24
MM = (seg_final % 3600) // 60
SS = seg_final % 60

print(f"Hora de llegada: {HH:02}:{MM:02}:{SS:02}")