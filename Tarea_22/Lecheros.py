# definimos variable para indicar el número de vacas que hay a la venta en Tolosa
vacas_Tolosa=int(input("Introduce el número total de vacas a la venta en Tolosa:  "))
# definimos la variable filas ya que por cada vaca tendremos: peso, leche, leche/peso, nº de vaca.
filas=4
# total será el número de datos totales que tendremos
total=vacas_Tolosa*filas
total1=total/4
# definimos un array con el numero de vacas que tenemos
numero_vacas=[]
for i in range(0,vacas_Tolosa):
	numero_vacas.append(i+1)

#definimos otros array que usaremos para ordenar las vacas por mejor rendimiento ( l/Kg) 
vacas=[]
for i in range(0,total):
	vacas.append(i)

#definimos un array para todos los datos que vamos a meter de las vacas 
vacas_inicial=[]
for i in range(0,total):
	vacas_inicial.append(i)

# Bucle para ir introduciendo las características de las vacas
i=0
j=0
while i<total: 

	print("Introduca el peso de la vaca", j+1)
	vacas[i]=vacas_inicial[i]=float(input())
	i=i+1
	print("Introduca la cantidad de leche que da la vaca", j+1)
	vacas[i]=vacas_inicial[i]=float(input())
	i=i+1
	Peso1=vacas_inicial[i-2]=vacas[i-2]
	Leche1=vacas_inicial[i-1]=vacas[i-1]
	Densidad=Leche1/Peso1
	vacas[i]=vacas_inicial[i]=Densidad
	i=i+1
	vacas[i]=vacas_inicial[i]=j+1
	i=i+1
	j=j+1


#definimos la variable para meter la capacidad del camión
camion=float(input(" Qué capacidad de carga tiene el camión en kilos ?  "))

print("")

# Bucle que calcula el peso de todas las vacas ##PROBADO
peso=0
peso1=0
for i in range(vacas_Tolosa):
	peso=vacas_inicial[4*(i-1)]
	peso1=peso1+peso

# Bucle que calcula el peso mínimo de toda la serie de las vacas ##PROBADO
peso_vacas=[] # variable donde metemos todos los pesos de las vacas
for i in numero_vacas:
	peso_vacas.append(vacas_inicial[4*(i-1)]) # vamos añadiendo a la lista los valores de los pesos
a=min(peso_vacas) # variable con el valor mínimo de peso

# Bucle que te dirá si no hay vacas que entren en el camión ##PROBADO
if camion < a:
	print("No hay ninguna vaca que entre en el camión")

# Bucle que analiza si todas las vacas  entran en el camión	 ##PROBADO
elif peso1<=camion:
	print("Todas las vacas entran en el camión")

# Bucle que analiza que hacer si todas las vacas  no entran en el camión
else:
	
	# Este for ordena las vacas de mayo a menor productividad l/Kg ## PROBADO

	j=1
	for j in range(vacas_Tolosa-1): 
		i=0
		for i in range(vacas_Tolosa-1):
			if(vacas[4*i+2]<vacas[4*i+6]):

				aux1=vacas[4*i]
				aux2=vacas[4*i+1]
				aux3=vacas[4*i+2]
				aux4=vacas[4*i+3]

				vacas[4*i]=vacas[4*i+4]
				vacas[4*i+1]=vacas[4*i+5]
				vacas[4*i+2]=vacas[4*i+6]
				vacas[4*i+3]=vacas[4*i+7]

				vacas[4*i+4]=aux1		
				vacas[4*i+5]=aux2		
				vacas[4*i+6]=aux3
				vacas[4*i+7]=aux4


	# Este for suma por orden el peso de las vacas ordenadas y detecta cuando se pasa de la capacidad del camión
	# PROBADO
	i=0
	j=0
	pesototal=0 
	peso=0

	for i in range (vacas_Tolosa): 	
		if pesototal <= camion:
			peso=vacas[4*i]
			pesototal=pesototal+peso
			j=j+1

	vacas_en_camion=j-1 # El número de vacas que han entrado en el camión
	vacas_en_camion1=j # El número de vacas que han entrado en el camión +1

	#For para calcular el margen que nos ha quedado en el camión ## PROBADO

	i=0
	peso1=0
	peso2=0

	for i in range (j-1): 
		peso1=vacas[4*i]
		peso2=peso2+peso1

	margen_camion=camion-peso2 


	# Si el peso total coincide con la capacidad del camión, problema solucionado # PROBADO

	if margen_camion==0: 

		exacto=[] # definimos variable para meter las vacas que coinciden justo
		leche=0
		leche_obtenida=0
		i=0
		i=0
		for i in range (0,j-1):
			justo=vacas[4*i+3] # definimos variable que cuenta el indice de la vaca que suma exacto
			exacto.append(vacas[4*i+3])
			leche=vacas[4*i+1]
			leche_obtenida=leche_obtenida+leche
			
		print( " La capacidad máxima de leche se obtiene cargando  las vacas: ",exacto,"y la leche obtenida son: ", leche_obtenida,  "litros")

	else: 

	# Vamos a dividir todas las vacas en tres grupo:
		# Vacas que seguro estarán en el camion y no hace falta probar: "Vacas Top"
		# Vacas que en un principio no estarán en el camion y no hace falta probar al principio: "Vacas Full"
		# El resto de vacas que empezaremos a combinar.

	# Empezamos a seleccionar las vacas Top

		i=0
		z=0
		w=0
		a=0
		top=[]

		for i in  range(0,vacas_en_camion): 
			if vacas[4*i]*vacas[4*i+2]>=(vacas[4*i]+margen_camion)*vacas[4*vacas_en_camion+2]:
				
				a=vacas[4*i+3]
				top.append(a)
				z=z+1
			
		vacas_en_camion_seguro=z # Variable que representa el número de vacas Top que hay

		# Cálculo de la leche y el peso de las vacas top

		i=0
		leche=0
		leche_top=0 # Variable que almacenará la leche de las vacas Top
		pesotop1=0 # Variable que almacenará el peso de las vacas Top
		pesotop2=0

		for i in top:
			leche=vacas_inicial[4*(i-1)+1]
			leche_top=leche_top+leche
			pesotop1=vacas_inicial[4*(i-1)]
			pesotop2=pesotop2+pesotop1

		
		## Seleccionamos las vacas Full.

		# Calculamos primero el peso disponible en el camion quitando lo que pesan las Top

		camion_inicial=0
		camion_inicial_1=0 # peso de las vas vacas que han entrado y no son Top
		camion_inicial_2=0 # peso camion_inicial_1 + el margen que había quedado en el camion llenando hasta que no entren más
		leche_inicial_1=0 
		leche_inicial_2=0
		b=0
		c=0
		d=0
		full=[] # array en el que estará las vacas full
		pesofull=[] # array en el que estará el peso de las vacas full
		lechefull=[] # array en el que estará la cantidad de leche de cada vaca full
		full1=full.copy() # array de vacas ful
		top1=top.copy() # array de vacas full que usaremos cuando pasemos a ver qué full-s podemos meter
					 # el mínimo de las full coincida con el marge que queda

		i=0

		for i in range(vacas_en_camion_seguro, vacas_en_camion): # vacas top , vacas en camion

			camion_inicial=vacas[4*i]
			camion_inicial_1=camion_inicial_1+camion_inicial
			leche_inicial_1=vacas[4*i+1]
			leche_inicial_2=leche_inicial_1+leche_inicial_2

		camion_inicial_2=margen_camion+camion_inicial_1 


		# Seleccionamos las vacas que no hay que meter seguro en el camion

		for i in range(vacas_en_camion,vacas_Tolosa):

			if vacas[4*i]>=camion_inicial_2 or vacas[4*i+1]+(camion_inicial_2-vacas[4*i])*vacas[(vacas_en_camion*4)+2]<=leche_inicial_2:

				b=vacas[4*i+3]
				full.append(b)
				c=vacas[4*i]
				pesofull.append(c)
				d=vacas[4*i+1]
				lechefull.append(d)
			
	# definimos el array de las vacas que no hay que analizar
		noanalizar=top+full


	# borramos del array numero_vacas las que no hay que analizar par sacar las que sí
		i=0
		for i in noanalizar:
			numero_vacas.remove(i)


	# sacamos ( si interesa) por pantalla las listas de vacas top,full 
		#print("Vacas top",top)
		#print("Vacas full",full)
		#print("Vacas posibles a combinar",numero_vacas)
		

	# calculamos el peso de las vacas a combinar
		peso_vacas_combinar=0	
		peso_vacas_combinar1=0

		for i in numero_vacas:
			peso_vacas_combinar=vacas_inicial[4*(i-1)]
			peso_vacas_combinar1=peso_vacas_combinar1+peso_vacas_combinar

		
#############################################################################################################

	# bucle que calcula que hacer si no hay vacas a combinar
		if peso_vacas_combinar1 == 0 :
		
			# metemos la condición dependiendo del valor del mínimo peso de las vacas full
		
			#a=0
			a=min(pesofull) # Variable que determina el mínimo peso que tienen las vacas full
			if a > camion_inicial_2: # si el mínimo de las full es > que el margen, solo entran las top
				print( " Las vacas que debes cargar en el camión son ", top, " y darán" , leche_top, " litros de leche.")
			elif a == camion_inicial_2: # si el mínimo es igual al margen, lo sumamos
				e=0
				e=full[pesofull.index(camion_inicial_2)] # nos devuelve la vaca que tiene el peso min
				top1.append(e) # le añadimos esta vaca al array de las Top
				f=0
				f=lechefull[pesofull.index(camion_inicial_2)] # nos devuelve la leche de la vaca que tiene el peso min
				leche_topfull=0 # variable para sumar la leche top y full que entrará
				leche_topfull=leche_top+f
				print("Las vacas que debes cargar en el camion son",top1,"y la leche que darán es: ",leche_topfull)
				
			else: 
				# hacemos las combinaciones de las vacas full y sacamos la que mejor leche y que entre en el camion
				# sacamos la lista de pesos de las vacas a combinar
				subfull1=[] # creamos una lista con las combinaciones de las vacas 
				subpesofull=[] #creamos una lista con el peso de las vacas a combinar
				subpesofull1=[] #creamos una lista con las combinaciones del peso de las vacas a combinar
				sublechefull=[] # cramos una lista con la leche de las vacas a combinar
				sublechefull1=[] # cramos una lista con las combinaciones de la leche de las vacas a combinar
				sumaleche1=0 # definimo la variable que usaremos para elegir la combinación que de el máximo de leche
				sumaleche=0
				sumapeso=0
				sumapeso1=0 # variable que guardará el valor de peso de la mejor combinación
				vacas_full1=[] # variable para la lista de las vacas elegidas dentro de las de combinar
				for i in full:
					r=vacas_inicial[4*(i-1)]
					subpesofull.append(r) # en esta lista metemos los pesos de las vacas full
					s=vacas_inicial[4*(i-1)+1]
					sublechefull.append(s) # en esta lista metemos la leche de las vacas full
					
				from itertools import combinations
				
				for i in range(0,len(full)):
					subcombinar=list(combinations(full,i)) # creamos las combinaciones de las vacas posibles
					subpesofull2=list(combinations(subpesofull,i)) # creamos las combinaciones de los pesos posibles
					sublechefull2=list(combinations(sublechefull,i)) # creamos las combinaciones de las leches posibles
					if len(subcombinar)>0:
						subfull1.extend(subcombinar)
					if len(subpesofull)>0:
						subpesofull1.extend(subpesofull2)
					if len(sublechefull)>0:
						sublechefull1.extend(sublechefull2)

				for i in range ( 0, len(sublechefull1)): # bucle que calcula el maximo de leche que da la combinacion
															 # que sume menos o igual que el margen que tenemos en el camion
						sumaleche=sum(sublechefull1[i])
						sumapeso=sum(subpesofull1[i])
						vacas_combinar=subfull1[i]
						
						if sumapeso<=camion_inicial_3 and sumaleche>sumaleche1:
							sumaleche1=sumaleche
							vacas_full1=vacas_combinar
							sumapeso1=sumapeso
							

				camion_inicial4=camion-pesotop2 # definimos variable para calcular el margen que hay en el camión
				margen_camion6=camion_inicial_4-sumapeso1 # margen del camion -`peso vacas top-peso vacas combinadas

				vacas_full2=list(vacas_full1)+final
				leche_full2=sumaleche1+leche_final1

				print( " las vacas que debes cargar son", vacas_full2, " y darán ", leche_full2," litros de leche.")

	# bucle que calcula que hacer si el peso de las vacas a combinar es menor que el margen, ### faltaría sumar posibles full
		if peso_vacas_combinar1<=camion_inicial_2 and peso_vacas_combinar1!=0:

			peso_final=0
			peso_final1=0
			leche_final=0
			leche_final1=0
			camion_inicial_3=0 # Variable que marca el margen que queda para las vacas full

			final=top+numero_vacas # array con vacas top y vacas a combinar

			

			for i in final:

				peso_final=vacas_inicial[4*(i-1)]
				peso_final1=peso_final1+peso_final
				leche_final=vacas_inicial[4*(i-1)+1]
				leche_final1=leche_final1+leche_final

			camion_inicial_3=camion-peso_final1 # variable para saber el margen que queda despues de meter todas las combinables

			# vamos a analizar como gestionamos las vacas full.
			# eliminaremos las vacas que son mayores del margen que queda " camion_inicial3"
			full1=[] # variable de las vacas full que son menores del margen que hay
			fullleche1=[] # leche de las vacas full1
			pesofull1=[] # peso de las vacas full1
			for i in full:
				if vacas_inicial[4*(i-1)]<=camion_inicial_3:
					full1.append(i)
					g=vacas_inicial[4*(i-1)+1]
					fullleche1.append(g)
					h=vacas_inicial[4*(i-1)]
					pesofull1.append(h)

			# empezamos a marcar condicionales en funcion de la longitud de la lista de full1

			if len(full1)==0: #PROBADO si no hay nada en full1 entonces no hace fakta sumar nada
				print( " Las vacas que debes cargar en el camión son ", final, " y darán" , leche_final1, " litros de leche.")
			
			elif len(full1)==1: #PROBADO si solo hay una hay que sumar esa
				final2=final+full1 # definimos la lista en la que se suma la vaca full que cumple
				fullleche2=leche_final1+g # definimo la cantidad de leche después de sumar la leche de la full que cumple
				print( " Las vacas que debes cargar en el camión son ", final2, " y darán" , fullleche2, " litros de leche.")
			elif len(full1)>1: # si hay más de dos debemos de discriminar si la suma de dos cualquiera es mayor
							# que el margen
				if 2*min(pesofull1)>camion_inicial_3: # PROBADO si dos veces el mínimo del peso es menor que el margen
					l=max(fullleche1)
					m=fullleche1.index(l)
					n=full1[m] 
					#final3=[] # definimos variable para añadir la vaca full que más leche da
					final.append(n)
					fullleche3=leche_final1+vacas_inicial[4*(n-1)+1]
					print( " Las vacas que debes cargar en el camión son ", final, " y darán" , fullleche3, " litros de leche.")
				else:
								# sacamos la lista de pesos de las vacas a combinar
					subfull1=[] # creamos una lista con las combinaciones de las vacas 
					subpesofull=[] #creamos una lista con el peso de las vacas a combinar
					subpesofull1=[] #creamos una lista con las combinaciones del peso de las vacas a combinar
					sublechefull=[] # cramos una lista con la leche de las vacas a combinar
					sublechefull1=[] # cramos una lista con las combinaciones de la leche de las vacas a combinar
					sumaleche1=0 # definimo la variable que usaremos para elegir la combinación que de el máximo de leche
					sumaleche=0
					sumapeso=0
					sumapeso1=0 # variable que guardará el valor de peso de la mejor combinación
					vacas_full1=[] # variable para la lista de las vacas elegidas dentro de las de combinar
					for i in full:
						r=vacas_inicial[4*(i-1)]
						subpesofull.append(r)
						s=vacas_inicial[4*(i-1)+1]
						sublechefull.append(s)
					
					from itertools import combinations
				
					for i in range(0,len(full)):
						subcombinar=list(combinations(full,i)) # creamos las combinaciones de las vacas posibles
						subpesofull2=list(combinations(subpesofull,i)) # creamos las combinaciones de los pesos posibles
						sublechefull2=list(combinations(sublechefull,i)) # creamos las combinaciones de las leches posibles
						if len(subcombinar)>0:
							subfull1.extend(subcombinar)
						if len(subpesofull)>0:
							subpesofull1.extend(subpesofull2)
						if len(sublechefull)>0:
							sublechefull1.extend(sublechefull2)

					for i in range ( 0, len(sublechefull1)): # bucle que calcula el maximo de leche que da la combinacion
															 # que sume menos o igual que el margen que tenemos en el camion
							sumaleche=sum(sublechefull1[i])
							sumapeso=sum(subpesofull1[i])
							vacas_combinar=subfull1[i]
							if sumapeso<=camion_inicial_3 and sumaleche>sumaleche1:
								sumaleche1=sumaleche
								vacas_full1=vacas_combinar
								sumapeso1=sumapeso
								
				
					vacas_full2=list(vacas_full1)+final
					leche_full2=sumaleche1+leche_final1

					print( " las vacas que debes cargar son", vacas_full2, " y darán ", leche_full2," litros de leche. ")


			

# bucle que calcula que hacer si el peso de las vacas a combinar es mayor que el margen, 
		if peso_vacas_combinar1>camion_inicial_2:
			# vamos a analizar como gestionamos las vacas combinar.
			# eliminaremos las vacas que son mayores del margen que queda " camion_inicial2"
			combinar1=[] # variable de las vacas a combinar 
			combinarleche1=[] # leche de las vacas combinar
			pesocombinar1=[] # peso de las vacas combinar
			for i in numero_vacas:
				if vacas_inicial[4*(i-1)]<=camion_inicial_2:
					combinar1.append(i)
					g=vacas_inicial[4*(i-1)+1]
					combinarleche1.append(g)
					h=vacas_inicial[4*(i-1)]
					pesocombinar1.append(h)

# empezamos a marcar condicionales en funcion de la longitud de la lista de combinar1

			if len(combinar1)==1: # si solo hay una hay que sumar esa
				final2=final+combinar1 # definimos la lista en la que se suma la vaca combinar que cumple
				combinarleche2=leche_top+g # definimo la cantidad de leche después de sumar la leche de la full que cumple
				print( " Las vacas que debes cargar en el camión son ", final2, " y darán" , combinarleche2, " litros de leche. ")
			
			elif len(combinar1)==2: # si hay dos y la suma es mayor que el margen debemos elegir el que más leche da
				combinarleche2=max(combinarleche1) # definimos la variable que nos coge la vaca que tiene la que más leche
				posicion2=combinarleche1.index(combinarleche2) # posición en la que está el peso máximo
				combinar2=combinar1[posicion2]
				topcombinar=top
				topcombinar.append(combinar2) # es la nueva lista añadiendo a las vacas top la elegida de las combinables
				combinarleche2=leche_top+combinarleche2
				print("Las vacas a introducir son:  ", topcombinar, " y darán", combinarleche2," litros de leche.") ## falta añadir la leche que darán
			else:	
				# sacamos la lista de pesos de las vacas a combinar
				subcombinar1=[] # creamos una lista con las combinaciones de las vacas 
				subpesocombinar=[] #creamos una lista con el peso de las vacas a combinar
				subpesocombinar1=[] #creamos una lista con las combinaciones del peso de las vacas a combinar
				sublechecombinar=[] # cramos una lista con la leche de las vacas a combinar
				sublechecombinar1=[] # cramos una lista con las combinaciones de la leche de las vacas a combinar
				sumaleche1=0 # definimo la variable que usaremos para elegir la combinación que de el máximo de leche
				sumaleche=0
				sumapeso=0
				sumapeso1=0 # variable que guardará el valor de peso de la mejor combinación
				vacas_combinar1=[] # variable para la lista de las vacas elegidas dentro de las de combinar
				for i in numero_vacas:
					r=vacas_inicial[4*(i-1)]
					subpesocombinar.append(r)
					s=vacas_inicial[4*(i-1)+1]
					sublechecombinar.append(s)
					
				from itertools import combinations
				
				for i in range(0,len(numero_vacas)):
					subcombinar=list(combinations(numero_vacas,i)) # creamos las combinaciones de las vacas posibles
					subpesocombinar2=list(combinations(subpesocombinar,i)) # creamos las combinaciones de los pesos posibles
					sublechecombinar2=list(combinations(sublechecombinar,i)) # creamos las combinaciones de las leches posibles
					if len(subcombinar)>0:
						subcombinar1.extend(subcombinar)
					if len(subpesocombinar)>0:
						subpesocombinar1.extend(subpesocombinar2)
					if len(sublechecombinar)>0:
						sublechecombinar1.extend(sublechecombinar2)

				for i in range ( 0, len(sublechecombinar1)): # bucle que calcula el maximo de leche que da la combinacion
															 # que sume menos o igual que el margen que tenemos en el camion
						sumaleche=sum(sublechecombinar1[i])
						sumapeso=sum(subpesocombinar1[i])
						vacas_combinar=subcombinar1[i]
						if sumapeso<=camion_inicial_2 and sumaleche>sumaleche1:
							sumaleche1=sumaleche
							vacas_combinar1=vacas_combinar
							sumapeso1=sumapeso
							
				margen_camion4=camion_inicial_2-sumapeso1 # margen del camion -`peso vacas top-peso vacas combinadas

				vacas_combinar2=list(vacas_combinar1)+top
				leche_combinar2=sumaleche1+leche_top
				sumapeso2=sumapeso1+pesotop2 # variable que almacena el peso de la suma de las top + combinadas
				margen_camion7=camion-sumapeso2 # variable que calcula el margen que queda para ver si entran fulls
				
				# vamos a analizar como gestionamos las vacas full.
				# eliminaremos las vacas que son mayores del margen que queda " camion_inicial3"
				full1=[] # variable de las vacas full que son menores del margen que hay
				fullleche1=[] # leche de las vacas full1
				pesofull1=[] # peso de las vacas full1
				for i in full:
					if vacas_inicial[4*(i-1)]<=margen_camion7:
						full1.append(i)
						g=vacas_inicial[4*(i-1)+1]
						fullleche1.append(g)
						h=vacas_inicial[4*(i-1)]
						pesofull1.append(h)

				# empezamos a marcar condicionales en funcion de la longitud de la lista de full1

				if len(full1)==0: # PROBADO si no hay nada en full1 entonces no hace fakta sumar nada
					print( " las vacas que debes cargar son", vacas_combinar2, " y darán ", leche_combinar2," litros de leche.")

				elif len(full1)==1: # PROBADO si solo hay una hay que sumar esa
					final2=vacas_combinar2+full1 # definimos la lista en la que se suma la vaca full que cumple
					fullleche2=leche_combinar2+g # definimo la cantidad de leche después de sumar la leche de la full que cumple
					print( " Las vacas que debes cargar en el camión son ", final2, " y darán" , fullleche2, " litros de leche.")

				elif len(full1)>1: # si hay más de dos debemos de discriminar si la suma de dos cualquiera es mayor
							# que el margen
					if 2*min(pesofull1)<margen_camion7: # si dos veces el mínimo del peso es menor que el margen
						l=max(fullleche1)
						m=fullleche1.index(l)
						n=full1[m] 
						vacas_combinar2.append(n)
						fullleche3=leche_combinar2+vacas_inicial[4*(n-1)+1]
						print( " Las vacas que debes cargar en el camión son ", vacas_combinar2, " y darán" , fullleche3, " litros de leche.")

					else:
								# sacamos la lista de pesos de las vacas full
						subfull1=[] # creamos una lista con las combinaciones de las vacas 
						subpesofull=[] #creamos una lista con el peso de las vacas a combinar
						subpesofull1=[] #creamos una lista con las combinaciones del peso de las vacas full
						sublechefull=[] # cramos una lista con la leche de las vacas a combinar
						sublechefull1=[] # cramos una lista con las combinaciones de la leche de las vacas full
						sumaleche1=0 # definimo la variable que usaremos para elegir la combinación que de el máximo de leche
						sumaleche=0
						sumapeso=0
						sumapeso1=0 # variable que guardará el valor de peso de la mejor combinación
						vacas_full1=[] # variable para la lista de las vacas elegidas dentro de las full
						for i in full:
							r=vacas_inicial[4*(i-1)]
							subpesofull.append(r)
							s=vacas_inicial[4*(i-1)+1]
							sublechefull.append(s)
					
						from itertools import combinations
				
						for i in range(0,len(full)):
							subcombinar=list(combinations(full,i)) # creamos las combinaciones de las vacas posibles
							subpesofull2=list(combinations(subpesofull,i)) # creamos las combinaciones de los pesos posibles
							sublechefull2=list(combinations(sublechefull,i)) # creamos las combinaciones de las leches posibles
							if len(subcombinar)>0:
								subfull1.extend(subcombinar)
							if len(subpesofull)>0:
								subpesofull1.extend(subpesofull2)
							if len(sublechefull)>0:
								sublechefull1.extend(sublechefull2)

						for i in range ( 0, len(sublechefull1)): # bucle que calcula el maximo de leche que da la combinacion
															 # que sume menos o igual que el margen que tenemos en el camion
							sumaleche=sum(sublechefull1[i])
							sumapeso=sum(subpesofull1[i])
							vacas_combinar=subfull1[i]
							vacas_full1=[]
							if sumapeso<=margen_camion7 and sumaleche>sumaleche1:
								sumaleche1=sumaleche
								vacas_full1=vacas_combinar
								sumapeso1=sumapeso
				
						vacas_full2=list(vacas_full1)+vacas_combinar2
						leche_full2=sumaleche1+leche_combinar2

						print( " las vacas que debes cargar son", vacas_full2, " y darán ", leche_full2," litros de leche.")









