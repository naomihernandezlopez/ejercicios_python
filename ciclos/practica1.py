#programa que calcula el factorial de un numero 
#con for 
#5 factorial = 1*2*3*4*5

num = int(input("Ingresa un numero: "))

factorial = 1
for i in range(1, num + 1):
	factorial = factorial *i

print('El factorial de', num,'es',factorial)