# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:25:25 2021

@author: x1jferre
"""

# Función para crear una lista a partir de los número que se meten por teclado
# hasta introducir un 0
def listar():
    lista=[]
    z=1
    while z!=0:
        z=int(input("Introduzca el nuevo número.\n"))
        if z!=0:
            lista.append(z)
        else:
            pass
    return lista

lista=listar()
print("La lista creada es:",lista)

# Introducción por pantalla de un número que quitaremos de la lista
numero=int(input("Ingrese un número que se eliminará de la lista:\n"))

lista1=lista.copy()
try:
    lista1.remove(numero)
except ValueError:
    print("El número",numero, "no está en la lista.")
print("La lista modificada quitando el numero",numero,"es:\n",lista1)

# Suma de los elemento que han quedado en la lista1

for i in range(len(lista1)):
    if i==0:
        suma=lista1[i]
    else:
        suma=suma+lista1[i]

print("La suma de los elementos de esta última lista son:",suma)

# Creación de una lista de los valores que son < de un número introducido por teclado
numero1=int(input("Ingrese un nuevo número:\n"))
lista2=[]
for i in range(len(lista)):
    if lista[i]<numero1:
        lista2.append(lista[i])
    else:
        pass
print("La lista modificada teniendo en cuenta solo los valores menores de",numero1,"es:\n",lista2,"\n")

# Definición de la función que crea una lista en la que se indica cuantas ocasiones
# en las que se repite cada número
lista4=[]


def conteo(lista):
    try:
        contador=0
        z=lista[0]
        posicion=[]
        for i in range(len(lista)):
            if lista[i]==z:
                contador=contador+1
                posicion.append(i)
            else:
                pass
        lista4.append((z,contador))
        posicion.reverse()
        posicion1=tuple(posicion)
        for j in posicion1:
            lista.pop(j)
        conteo(lista)
        
    except IndexError:
        pass

    return lista4

print("El número de veces en los que aparece cada número en la lista es:\n")
print(conteo(lista))


