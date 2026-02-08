#Algoritmo que pida un número y diga si es positivo, negativo o 0.




numero = int(input('Ingresa un numero: '))

if numero == 0:
    print('El numero es Cero:')
else:
    if numero > 0:
        print('El numero es positivo')
    else: 
     print('El numero es negativo')