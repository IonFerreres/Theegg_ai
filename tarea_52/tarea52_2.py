# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:59:45 2021

@author: x1jferre
"""
contador1=0
contador2=0
nombres_primario=set()
nombres_secundario=set()

while contador1!=1:
    nombrep=input("Introduzca el nombre del alumno de primario ( Si no desea introducir ninguno más indique x) :\n")
    if nombrep!="x":
        nombres_primario.add(nombrep)
    else:
        contador1=1

while contador2!=1:
    nombres=input("Introduzca el nombre del alumno de secundaria ( Si no desea introducir ninguno más indique x):\n")
    if nombres!="x":
        nombres_secundario.add(nombres)
    else:
        contador2=1

nombres=nombres_primario | nombres_secundario
nombres_comun=nombres_primario & nombres_secundario
nombres1=nombres_primario-nombres_secundario

print("Los alumnos de nivel primario y secundario son:\n",nombres)
print("Los nombres",nombres_comun,"se repiten entre alumnos de nivel primario y secundario. ")
print("Los nombres",nombres1,"de nivel priario, no se repiten en nivel secundario.")