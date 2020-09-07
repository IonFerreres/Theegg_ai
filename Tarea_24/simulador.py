# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:07:13 2020

@author: x1jferre
"""
z=int(input("Introduzca el número que desea pasar a binario:   "))

def simulador(decimal):
    
    binario=[] ##lista para definir la longitud que tendrá el numero en binario
    
    i=0
    
    for i in range(decimal):
        if sum(binario)<decimal:
            binario.append(2**i)
    binario.reverse() # cambiamos el orden para que tenga el mismo que el número
    
    i=0
    
    binario1=binario.copy() # lista en la que estarán el binario
    # binario1[0]=1
    suma1=0
    for i in range(len(binario)): # for para in costruyendo la lista que representará el numero en binario
        suma=suma1+binario[i]
        if suma<=decimal:
            suma1=suma
            binario1[i]=1
        else:
            binario1[i]=0
    
    binario2="".join([str(_) for _ in binario1]) # pasamos la lista a número
    return(binario2)

print(simulador(z)) 
    