Mensaje=input("Introduce el mensaje a cifrar ( en mayusculas ):  ")

def solitario(Mensaje):

	##Mensaje=input("Introduce el mensaje a cifrar:  ")
	Mensaje1=[] # convertimos a lista el mensaje, cada item será una letra o espacio
	i = ""
	for i in Mensaje:
		if i != " ":
			Mensaje1.append(i)

	j=len(Mensaje1) # almacena la longitud de la frase sin espacios

	k=int(j/5) # almacena el numero de huecos que debemos introducir

	l=0 # variable para correr un valor la introducción de espacio cada 5 letras

	if k>=1: # si el valor de huecos es igual a 1 o mayor metemos espacios cada 5 letras
		for i in range(1,k+1):
			Mensaje1.insert(5*i+l,"")
			l=l+1
	else: # si el valor es menor a uno metemos el espacio en la posición 5
		Mensaje1.insert(5,"")

	baraja = [] # lista que almacena las cartas de la baraja ordenada del 1 al 53

	for i in range (1,54):
		baraja.append(i)

	import random

	global clave # definimos lista global que será la clave=orden de la baraja que usaremos para encri-desencri
	clave1=random.sample(baraja,53) # La clave será la baraja ordenada de una cierta manera aleatoria    
	clave=clave1.copy()
	#print(clave1)
	#print(Mensaje)

	u=0

	encriptado1=[] # lista que usaremos para generar la lista creada con solitario


	for i in Mensaje:
		
		if i.isspace():
			v=1
		else:
			# iniciamos la conversión con el solitario
			# 1 Intercambiamos la carta comodin A con la que tiene detrás. Si esta en la última posición se mete en la segunda
			posicion1=int(clave1.index(52))
			if posicion1!= 52:
				clave1[posicion1]=clave1[posicion1+1]
				clave1[posicion1+1]=52
			else:
				clave1.remove(52)
				clave1.insert(1,52)
			
     
			# 2 Intercambiamos la carta comodin B con la que tiene detrás de la de detrás
			posicion2=int(clave1.index(53))



			if posicion2<51:
				clave1[posicion2]=clave1[posicion2+1]
				clave1[posicion2+1]=clave1[posicion2+2]
				clave1[posicion2+2]=53
			elif posicion2==51:
			    clave1.remove(53)
			    clave1.insert(1,53)
			else :
			    clave1.remove(53)
			    clave1.insert(2,53)

			

			# 3 intercambiamos los valores de la lista que están antes y después de los comodines
			posicion1=int(clave1.index(52))
			posicion2=int(clave1.index(53)) 
			lista1=[]
			lista2=[]
			lista3=[]

			

			if posicion1<posicion2:
				lista1=clave1[0:posicion1]
				lista2=clave1[posicion1:posicion2+1]
				lista3=clave1[posicion2+1:53]

			if posicion1>posicion2:
			    lista1=clave1[0:posicion2]
			    lista2=clave1[posicion2:posicion1+1]
			    lista3=clave1[posicion1+1:53]

			clave1=lista3+lista2+lista1

			
			# 4 cogemos la última carta y contando desde la primera cortamos por la siguiente al numero de la última.
			# pero mantenemos la última

			k=clave1[52]

			lista1=clave1[0:k]
			lista2=clave1[k:52]
			lista3=clave1[52]

			clave1=lista2+lista1
			
			
			clave1.append(lista3)

			
			# 5 cogemos la primera carta y contando desde la primera eleguimos la que esta después de la posición que marca la primera.

			l=clave1[0]
			
			carta=clave1[l-1]

			
			cifrado=[]
			cifrado.append(carta)
			
			abecedario=["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # definimos abecedario que usaremos para pasar de número
			

		
			encriptado1.append(abecedario[carta]) # añadimos la primera letra conseguida en solitario
	    	
				
			

	j=len(encriptado1) # almacena la longitud de la frase sin espacios

	k=int(j/5) # almacena el numero de huecos que debemos introducir

	l=0 # variable para correr un valor la introducción de espacio cada 5 letras

	if k>=1: # si el valor de huecos es igual a 1 o mayor metemos espacios cada 5 letras
		for i in range(1,k+1):
			encriptado1.insert(5*i+l,"")
			l=l+1
	else: # si el valor es menor a uno metemos el espacio en la posición 5
		encriptado1.insert(5,"")		


	encriptado1numero=[] # lista en la que almacenamos el encriptado1 en numeros
	Mensaje1numero=[] # lista en la que almacenamos el mensaje1 en numeros


	for i in range(len(encriptado1)):
		encriptado1numero.append(abecedario.index(encriptado1[i]))
		Mensaje1numero.append(abecedario.index(Mensaje1[i]))


	# Sacamos la lista suma de los dos mensajes codificados pasada a numero	
	sumamensajeencriptado=[]

	for i in range(len(Mensaje1)):
		suma=Mensaje1numero[i]+encriptado1numero[i]
		
		if suma<=27:
		
			sumamensajeencriptado.append(suma)
		else:
			suma1=suma-27
			sumamensajeencriptado.append(suma1)


	# convertimos la lista de numeros a letras

	sumamensaje1encriptado=[]

	for i in sumamensajeencriptado:

		sumamensaje1encriptado.append(abecedario[i])
	
	return print("".join(sumamensaje1encriptado))
	

solitario(Mensaje)  

##############################################################################################

def descifrar(Mensaje):

	global clave
	Mensaje=input("Introduce el mensaje a descifrar ( en mayusculas ):  ")
	Mensaje1=[] # convertimos a lista el mensaje, cada item será una letra o espacio
	i = ""
	for i in Mensaje:
		if i != " ":
			Mensaje1.append(i)

	j=len(Mensaje1) # almacena la longitud de la frase sin espacios

	k=int(j/5) # almacena el numero de huecos que debemos introducir

	l=0 # variable para correr un valor la introducción de espacio cada 5 letras

	if k>=1: # si el valor de huecos es igual a 1 o mayor metemos espacios cada 5 letras
		for i in range(1,k+1):
			Mensaje1.insert(5*i+l,"")
			l=l+1
	else: # si el valor es menor a uno metemos el espacio en la posición 5
		Mensaje1.insert(5,"")

	u=0

	encriptado1=[] # lista que usaremos para generar la lista creada con solitario


	for i in Mensaje:
		
		if i.isspace():
			v=1
		else:
			# iniciamos la conversión con el solitario
			# 1 Intercambiamos la carta comodin A con la que tiene detrás. Si esta en la última posición se mete en la segunda
			posicion1=int(clave.index(52))
			if posicion1!= 52:
				clave[posicion1]=clave[posicion1+1]
				clave[posicion1+1]=52
			else:
				clave.remove(52)
				clave.insert(1,52)
			     
			# 2 Intercambiamos la carta comodin B con la que tiene detrás de la de detrás
			posicion2=int(clave.index(53))

			if posicion2<51:
				clave[posicion2]=clave[posicion2+1]
				clave[posicion2+1]=clave[posicion2+2]
				clave[posicion2+2]=53
			elif posicion2==51:
			    clave.remove(53)
			    clave.insert(1,53)
			else :
			    clave.remove(53)
			    clave.insert(2,53)

			# 3 intercambiamos los valores de la lista que están antes y después de los comodines
			posicion1=int(clave.index(52))
			posicion2=int(clave.index(53)) 
			lista1=[]
			lista2=[]
			lista3=[]

			if posicion1<posicion2:
				lista1=clave[0:posicion1]
				lista2=clave[posicion1:posicion2+1]
				lista3=clave[posicion2+1:53]

			if posicion1>posicion2:
			    lista1=clave[0:posicion2]
			    lista2=clave[posicion2:posicion1+1]
			    lista3=clave[posicion1+1:53]

			clave=lista3+lista2+lista1

			# 4 cogemos la última carta y contando desde la primera cortamos por la siguiente al numero de la última.
			# pero mantenemos la última

			k=clave[52]

			lista1=clave[0:k]
			lista2=clave[k:52]
			lista3=clave[52]

			clave=lista2+lista1

			clave.append(lista3)

			# 5 cogemos la primera carta y contando desde la primera eleguimos la que esta después de la posición que marca la primera.

			l=clave[0]
			
			carta=clave[l-1]

			cifrado=[]
			cifrado.append(carta)
			
			abecedario=["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # definimos abecedario que usaremos para pasar de número
					
			encriptado1.append(abecedario[carta]) # añadimos la primera letra conseguida en solitario
	    			


	j=len(encriptado1) # almacena la longitud de la frase sin espacios

	k=int(j/5) # almacena el numero de huecos que debemos introducir

	l=0 # variable para correr un valor la introducción de espacio cada 5 letras

	if k>=1: # si el valor de huecos es igual a 1 o mayor metemos espacios cada 5 letras
		for i in range(1,k+1):
			encriptado1.insert(5*i+l,"")
			l=l+1
	else: # si el valor es menor a uno metemos el espacio en la posición 5
		encriptado1.insert(5,"")		


	encriptado1numero=[] # lista en la que almacenamos el encriptado1 en numeros
	Mensaje1numero=[] # lista en la que almacenamos el mensaje1 en numeros


	for i in range(len(encriptado1)):
		encriptado1numero.append(abecedario.index(encriptado1[i]))
		Mensaje1numero.append(abecedario.index(Mensaje1[i]))

		# Sacamos la lista resta  de los dos mensajes codificados pasada a numero	
	restamensajeencriptado=[]

	for i in range(len(Mensaje1)):
		if Mensaje1numero[i]==0 and encriptado1numero[i]==0:
			restamensajeencriptado.append(0)
		elif Mensaje1numero[i]<=encriptado1numero[i]:
			resta=Mensaje1numero[i]+27-encriptado1numero[i]
			restamensajeencriptado.append(resta)
		else:
			resta=Mensaje1numero[i]-encriptado1numero[i]
			restamensajeencriptado.append(resta)


	restamensaje1encriptado=[]

	for i in restamensajeencriptado:

		restamensaje1encriptado.append(abecedario[i])

	return print("".join(restamensaje1encriptado))
		
	
descifrar(Mensaje) 

