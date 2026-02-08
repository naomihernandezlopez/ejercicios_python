#Un alumno desea saber cual será su calificación final en la materia de Algoritmos
#Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.






# Programa para calcular la calificación final en Algoritmos

# Solicitar las calificaciones al usuario
parcial1 = float(input("Ingrese la primera calificación parcial: "))
parcial2 = float(input("Ingrese la segunda calificación parcial: "))
parcial3 = float(input("Ingrese la tercera calificación parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calcular promedio de parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# Calcular ponderaciones
ponderacion_parciales = promedio_parciales * 0.55
ponderacion_examen = examen_final * 0.30
ponderacion_trabajo = trabajo_final * 0.15

# Calificación final
calificacion_final = ponderacion_parciales + ponderacion_examen + ponderacion_trabajo

# Mostrar resultados
print(f"Promedio de parciales: {promedio_parciales:.2f}")
print(f"Ponderación de parciales (55%): {ponderacion_parciales:.2f}")
print(f"Ponderación del examen final (30%): {ponderacion_examen:.2f}")
print(f"Ponderación del trabajo final (15%): {ponderacion_trabajo:.2f}")

