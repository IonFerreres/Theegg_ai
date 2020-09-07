valor=int(input()) # Introducimos el valor N

for i in range(valor,1003002): # Iteramos entre el valor introducidoy y la 
# solución si introducimos el valor de 1000000              
    primo=i
    primo=list(str(primo))
    numero1=primo.copy()
    primo.reverse() # definimos una nueva variable que será el valor dado la vuelta
    # para analizar si es palíndromo
    if primo==numero1: # En el caso de que lo sea analizamos si es primo
        contador=0
        for j in range(1,i+1):
            if i%j==0:
                contador=contador+1
                if contador>2:
                    break
        if contador==2: # si es primo , damos en pantalla el valor y nos salimos
            primo=",".join(primo)
            primo=primo.replace(",","")
            print(primo)
            break
    

 
