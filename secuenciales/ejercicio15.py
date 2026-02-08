#Dadas dos variables numericas A y B, que el usuario debe teclear, 
#se pide realizar un algoritmo que intercambie los valores de ambas variables 
#y muestre cuanto valen al final las dos variables.




# Solicitar valores
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

# Intercambio usando variable auxiliar
aux = A
A = B
B = aux

print("Ahora A vale:", A)
print("Ahora B vale:", B)
