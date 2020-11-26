import re

texto= input("Introduzca el texto que quiere analizar :  ")

# Cálculo del número de caracteres
print("Total caracteres: "+ str(len(re.findall("[\w,\W]", texto))-len(re.findall("\s", texto))))

# Cálculo del número de palabra
print("Total palabras: "+str(len((re.split("\s",texto)))))

# Ranking de palabras
palabras= re.split("\s",texto)
muestra=[]

for palabra in palabras:
    if palabra!="":    
        muestra.append(palabras.count(palabra))

ranking=dict(zip(palabras,muestra))

import operator

ranking1=sorted(ranking.items(), key=operator.itemgetter(1),reverse=True)
print("El ranking de palabras por frecuencia es: " + str(ranking1))
         
   
   
    
    