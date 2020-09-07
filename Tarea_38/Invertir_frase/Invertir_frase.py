# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:45:33 2020

@author: x1jferre
"""
numero=int(input("Cuantas frases deseas analizar?   "))
total=[]

for i in range(numero):

    frase=input()
    frase=frase.split()
    frase.reverse()
    frase=",".join(frase)
    frase=frase.replace(","," ")
    total.append((frase))
    
j=len(total)

print("\n")

for i in range(j):
    print("Case  #"+str(i+1)+":    " + total[i] + "\n")

