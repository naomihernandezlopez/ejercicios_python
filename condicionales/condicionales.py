
#estructura de control if 
#if else elif

'''

if exp_booleana:
	instrucciones

if exp_booleana:
    instrucciones
else:
     instrucciones 

if exp_bool:
    instrucciones
elif exp_bool:
     instrucciones

else:
     instrucciones 
''' 

numero = int(input('Escribe un numero: '))

if numero > 0:
   print("Es un numero positivo")            
elif numero == 0:
	print('el numero es 0')
else: 
    print('es un numero negativo')	