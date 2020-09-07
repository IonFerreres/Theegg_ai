# ADN, con bases A,C,G,T

LISTA1=input("Introduzca la primera ristra de ADN:  ")
LISTA2=input("Introduzca la segunda ristra de ADN:  ")

def conversion(Lista): # función para convertir la lista ADN en múmeros
    NUMERO=[]
    for i in Lista:
        if i == "A":
            j=1
            NUMERO.append(j)            
        elif i == "C":
            j=2
            NUMERO.append(j)        
        elif i == "G":
            j=3
            NUMERO.append(j)        
        elif i == "T":
            j=4
            NUMERO.append(j)     
        else:
            print("El valor no es correcto")   
    return NUMERO

NUMERO1=conversion(LISTA1) # conversión del ADN1 a número
NUMERO2=conversion(LISTA2) # conversión del ADN2 a número

LNUMERO1=len(NUMERO1) # longitud de la lista número 1
LNUMERO2=len(NUMERO2) # longitud de la lista número 2

NUMERO3=(LNUMERO2-1)*[5]+NUMERO1 # secuencia convertida del ADN1 para poderlos comparar
NUMERO4=NUMERO2+(LNUMERO1-1)*[5] # secuencia convertida del ADN2 para poderlos comparar

#############################################################################

#Creamos la matriz con la primera secuencia de ADN , la de correvalores de la segunda secuencia del ADN2

import numpy as np

F2=np.vstack((NUMERO3,NUMERO4))

x=len(NUMERO4)-1 # definimos variable para contar las veces que debemos desplazar hacia la dcha el NUMERO4

for i in range(x): #   bucle para crear la matriz con la primera línea con el NUMERO 3 La segunda con el NUMERO 4 y luego 
#desplazadas cada vez un valor a la dcha insertando un 5 y borrando el de la dcha.
    NUMERO4.insert(0,5)    
    NUMERO4.pop()
    G=np.array([NUMERO4])
    F2=np.vstack((F2,G))

Tamaño=F2.shape
Filas=(Tamaño[0])+1 # variable para definir el número de líneas que llevará
# la matriz para restar

F3=NUMERO3

for i in range(Filas-2): # bucle para crear una matriz con todas las líneas
# con el numero 3
    F3=np.vstack((F3,NUMERO3))

F4=F2-F3 # matriz con la resta entre la primera ristra y las posibilidades con
# la segunda

ristra=[]
for i in range(len(NUMERO2)-1): # bucle para cera la lista con las posiciones
# de las columnas que hay que eliminar.
    ristra.append(i)

F5=np.delete(F4,ristra,axis=1) # eliminación de las columnas

x=F5.shape

filas=x[0]

# # bucle para añadir un uno al final de cada línea para contar el último cero

arreglo=np.array(filas*([1],))

F5=np.append(F5,arreglo, axis=1)

F5=np.delete(F5,0,axis=0)

# F5 es la matriz con la que debemos trabajar

x=F5.shape

filas=x[0]

# bucle para ir contando en cada línea cuantos ceros hay

ceros=[]
posicion=[]

for j in range(x[0]):
    
    ADN3=F5[j]
    k=0
    k1=0
    for i in ADN3: # bucle para calcular de cuantos ceros es la máxima lista
        if i !=0:
            if k<=k1:
                k=k1
                k1=0
            else:
                k1=0
        else:
            k1=k1+1        
    ceros.append(k)

maximo=max(ceros)
position=int(ceros.index(max(ceros)))
final=F5[position]

# Analizamos la línea en la que hay el número maáximo de ceros

ceros1=[]
posicion5=[]
   
k=0
k1=0

for i in final: # bucle para calcular de cuantos ceros es la máxima lista
    if i !=0:
        if k<=k1:
            k=k1
            k1=0
        else:
            k1=0
    else:
        k1=k1+1
   
j=0
j1=0
n=0

for i in final: # bucle para calcular en qué posición se encuentra la máxima lista
    
    if j1!=k:
        n=n+1    
        if i !=0:
            if j<=j1:
                j=j1
                j1=0
            else:
                j1=0
        else:
            j1=j1+1   

posicion1=n-1-k+1
posicion2=n-1
posicion5.append(posicion1)

suma=posicion1+k-1
posicion5.append(suma)

serie=NUMERO1[(posicion5[0]):(posicion5[1])+1]

########################################################################

# Conversion de lista numerica en secuencia de ADN
lista_adn=[]

for i in serie:
    if i == 1:
        j="A"
        lista_adn.append(j)            
    elif i == 2:
        j="C"
        lista_adn.append(j)        
    elif i == 3:
        j="G"
        lista_adn.append(j)        
    elif i == 4:
        j="T"
        lista_adn.append(j)     
    else:
        print("El valor no es correcto")   
   

lista_ADN="".join(lista_adn)

print( "\n"+lista_ADN)

