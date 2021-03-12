# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:56:12 2021

@author: x1jferre
"""
from timeit import default_timer
lista=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
valor=875
#############################################################################

# Algoritmo casero para ordenar una lista de números de menor a mayor valor
def ordenar(lista):
    for i in range (1,len(lista)):
        count=i
        def orden(lista,count):
            if lista[count]<lista[count-1]and count>0:
                A=lista[count-1]
                lista[count-1]=lista[count]
                lista[count]=A
                orden(lista,count-1)
            else:
                pass
        orden(lista,count)
    return lista
inicio=default_timer()
print(ordenar(lista))
fin=default_timer()
print(fin-inicio)
##############################################################################

# Algoritmo para búsqueda secuencial de un numero
def busqueda_secuencial(valor,lista):
    iteraciones=0
    for i in range (len(lista)):
        iteraciones=iteraciones+1
        if lista[i]==valor:
            print("BUSQUEDA SECUENCIAL")
            print("El número",valor,"está en la lista.")
            print("El número de iteraciones necesarias han sido",iteraciones)
            break
        elif i==(len(lista)-1):
            print("BUSQUEDA SECUENCIAL")
            print("El número",valor,"no está en la lista.")
            print("El número de iteraciones necesarias han sido",iteraciones)
            
inicio=default_timer()  
busqueda_secuencial(valor,lista) 
fin=default_timer()
print(fin-inicio)      
##############################################################################

# Algoritmo para búsqueda binaria de un numero
def busqueda_binaria(valor,lista,count):
    lista=ordenar(lista)
    try:    
        z= int(len(lista)/2)
        if lista[z]==valor: 
            print("BUSQUEDA BINARIA")
            print("El número",valor,"está en la lista.")
            print("El número de iteraciones necesarias han sido", count+1)
        elif valor < lista[z]:
            lista=lista[0:z]
            busqueda_binaria(valor, lista,count+1)
        else:
            lista=lista[(z+1):len(lista)]
            busqueda_binaria(valor, lista,count+1)
    except IndexError:
        print("BUSQUEDA BINARIA")
        print("El número",valor,"no se encuentra en la lista.")
        print("El número de iteraciones necesarias han sido",count+1)
  

inicio=default_timer()  
busqueda_binaria(valor,lista,0) 
fin=default_timer()
print(fin-inicio) 