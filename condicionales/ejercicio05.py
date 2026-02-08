#Escribe un programa que pida un nombre de usuario y una contraseña 
#y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
#sino se da un error.

user = 'admin'
password = 'qwerty'

usuario = input('Ingresa tu usuario: ')
contra = input('Ingresa tu contraseña: ')

if user == usuario and password == contra:
	print('Has entrado al sistema')
else:
    print('Error de acceso')	