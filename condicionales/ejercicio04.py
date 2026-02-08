# Crea un programa que pida al usuario dos números y muestre su división 
#si el segundo no es cero, o un mensaje de aviso en caso contrario.


num_1 = int(input('Ingresa un numero: '))
num_2 = int(input('Ingresa otro numero: '))

if num_2 == 0:
	print('No se puede dividir entre 0')
else:
    divi = num_1 / num_2	
    print('La division es:', divi)
