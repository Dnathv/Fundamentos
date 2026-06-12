# Programa: randint_A1                     20.03.26
# Autor: Dana Madai Gazca Loria
# Objetivo: Uso del modulo random.randint que genera numeros aleatorios
#   ademas aplicar "for in range ()"
# Problema: Ganerar e imprimir "n" numeros aleatorios en el rango
#   (inicial y final) indicando. Los valores son: inclusivo.
#   Los valores corresponden a edades de algunas personas.
# Se requiere importar la libreria random.

import random

print ("Se generan n numeroa aleatorios en el rango 17 a 25")
n = int(input("Cuantos numeros: "))

for x in range (n):              
    R = random.randint(1, 90)   # x = 0,1,3,4...n
    print (R, end = ' ')        # Pueden ser negativos (-10,5) 

print ("\nProceso Terminado")
