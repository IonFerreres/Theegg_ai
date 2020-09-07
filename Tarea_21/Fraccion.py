## Este programa muestra la fracción irreducible de un valor introducido por el usuario.
# El valor introducido debe estar entre los valores 0.0001 y 0.9999, ambos incluidos.

# Para asegurarnos que metemos bien los datos creamos un bucle while que analizará:
	# 1.- Si el dato que se mete no es un número o los decimales están separados por coma en lugar de punto.
	# 2.- Si el número que se mete tiene más de 4 decimales.
	# 3.- Si el número que se mete está en el intervalo 0.0001-0.9999.

a=1 # definimos la variable "a" que usaremos para detectar si el dato introducido no es un número o los decimales están separados 
	# por coma en lugar de punto.
k=0 # definimos la variable "k" que usaremos para contar la cantidad de decimales que tiene el número introducido.
Valor_Introducido1=0.5 # actualizamos el valor de la variable en la que almacenaremos el valor introducido para que no entre la 
					   # la primera ocasión en if dentro del while.


while a != 0 or k>6 or Valor_Introducido1 <0.0001 or Valor_Introducido1>0.9999:
# Mientras sea texto or tenga +4 decimales or no este en el rango 0.0001-0.9999

	if k>6:
		print("Debes introducir un número de cuatro decimales máximo") 

	if Valor_Introducido1<0.0001 or Valor_Introducido1>0.9999:
		print("El número debe estar entres 0.0001 y 0.9999, a.i.")

	try: # Le pedimos que introduzca el valor y lo guardamos primero en la variable Valor_Introducido como string
		 # y la pasamos a número como Valor_Introducido1.
		Valor_Introducido=input(" Introduzca el valor del que quiere calcular la fracción irreducible:  ")
		Valor_Introducido1=float(Valor_Introducido)
		k=0
		a=0
		for w in Valor_Introducido: # contamos cuantos caracteres tiene el valor introducido
			k=k+1
			
	except ValueError: # excepción en el que caso de que el dato que metememos no se pueda convertir a número
					   # actualizó el valor de la variable a=1 para que entre en el bucle.
					   # actualizo el valor de las variables k y Valor_Introducido 1 para que no entre en los if-s.
		print (" Debe introducir un número")
		a=1
		k=5
		Valor_Introducido1=0.5

# Para calcular la fracción	nos basamos en que la última fracción posible para conseguir el mínimo irreducible será el número/10000.
# como por ejemplo 0.9999, 9999/10000.
# Montamos un bucle for que irá recorriendo todas divisiones posibles empezando por el dividendo 1 recorriendo el divisisor de 1 
# hasta 10000. Una vez acabado con el 1 en dividendo pasaremos al valor 2 e inciamos el bucle.
# la primera división que consigamos que sea igual al valor metido será la fracción mínima y saldremos del bucle después de 
# imprimirlo por pantalla.



x=1
y=1
z=0
for x  in range(1,10001):
	for y in range(1,10001):
		if z != 1:
			fraccion=x/y
			if fraccion==Valor_Introducido1: # en cuanto la división coincida con el valor introducido nos salimos del bucle después 
											 # de imprimir en resultado.
				print("La fracción irreducible es", x , "/", y)
				z=1
		y=y+1
		if z ==1:
			break
	if z==1:
		break
x=x+1

